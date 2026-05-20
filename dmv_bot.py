import os
import csv
import time 
import random 
import logging 
import requests  # Added for native Discord HTTP webhook delivery
from datetime import datetime, timedelta 
from dotenv import load_dotenv 
from playwright.sync_api import sync_playwright

# Load secrets from the local .env file securely
load_dotenv()

# --- CONFIGURATION PROFILE ---
START_URL = "https://coloradoappt.cxmflow.com/Appointment/Index/d74f48b1-33a9-428c-acd1-d7d1bfc9555c"
MY_CURRENT_APPOINTMENT = datetime(2026, 6, 9) 
# This JUST checks for a date before this and does not take time into consideration. 
## For my needs, I am just looking for an earlier date. I do not care about the time 
## and my appointment is already early morning.   

## If you want the bot to check for *any* earlier day OR time slot on the day of the 
## appointment, use 24-hour format:
## Comment out the current MY_CURRENT_APPOINTMENT then uncomment the following:

# MY_CURRENT_APPOINTMENT = datetime(2026, 6, 9, 11, 15)

## NOTE FOR FORKS: If you switch to 24-hour format, you must also update the 
## parsing logic inside `parse_and_validate_date()` to match the full timestamp:
## Change: `found_date = datetime.strptime(date_part_only, "%m/%d/%Y")`
## To: `found_date = datetime.strptime(clean_timestamp_str, "%m/%d/%Y %I:%M %p")`

CSV_FILE_PATH = "dmv_appointment_trends.csv"
LOG_FILE_PATH = "dmv_master_log.txt"  # Unified master text log

LOCATIONS = [
    "Adams",
    "Aurora",
    "Centennial",
    "Denver NE",
    "Denver Regional Service Center",
    "Parker",
    "Westminster"
]

# --- UNIFIED LOGGING SYSTEM ---
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH, mode='a', encoding='utf-8'), # Appends to master log file
        logging.StreamHandler()                                         # Prints live inside your terminal
    ]
)

def init_csv_ledger():
    """Creates the data log CSV with structured tracking headers if it doesn't exist yet."""
    if not os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Scan Timestamp", "DMV Location", "Earliest Available Appointment Date"])
        logging.info(f"Initialized fresh data tracking ledger: {CSV_FILE_PATH}")

def log_data_point(location, date_str):
    """Appends a new data row to the trend spreadsheet."""
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        final_date_val = date_str if date_str else "No Slots Displayed"
        
        with open(CSV_FILE_PATH, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, location, final_date_val])
    except Exception as e:
        logging.error(f"Failed writing technical metrics to spreadsheet: {e}")

def human_delay(min_sec=1.5, max_sec=3.5):
    # Introduces natural micro-pauses between actions to mimic human behavior.
    time.sleep(random.uniform(min_sec, max_sec))

def send_discord_alert(location_name, appt_details):
    """Dispatches real-time markdown notifications straight to your private Discord channel via Webhook."""
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        logging.error("Notification dropped: DISCORD_WEBHOOK_URL is missing from your .env profile configuration.")
        return

    payload = {
        "content": (
            f"\U0001F6A8\U0001F6A8\U0001F6A8 **DMV MATCH FOUND!** \U0001F6A8\U0001F6A8\U0001F6A8\n"
            f"**Location:** {location_name}\n"
            f"**Details:** {appt_details}\n"
            f"⚡ *Claim it immediately! Remember to cancel your original booking first.* \n"
            f"@everyone"
        )
    }

    try:
        # Discord webhooks return a 204 No Content status code upon success
        response = requests.post(webhook_url, json=payload, timeout=10)
        if response.status_code == 204:
            logging.info(f"Discord Alert successfully sent for {location_name}!")
        else:
            logging.error(f"Discord server rejected payload with status code: {response.status_code}")
    except Exception as e:
        logging.error(f"Failed to post structured update alert to Discord client: {e}")

def parse_and_validate_date(calendar_text):
    """
    Parses strings matching the '6/11/2026 9:15 AM' pattern.
    Checks if the date is earlier than MY_CURRENT_APPOINTMENT AND ensures
    the appointment time is at least 60 minutes in the future to allow for travel time.
    """
    try:
        if not calendar_text or "/" not in calendar_text:
            return False, None
        
        # Clean white space from text target boundaries
        clean_timestamp_str = calendar_text.strip()
        
        # 1. Check if the date component is sooner than our current booking
        date_part_only = clean_timestamp_str.split(" ")[0]
        found_date = datetime.strptime(date_part_only, "%m/%d/%Y")
        is_sooner = found_date < MY_CURRENT_APPOINTMENT
        
        # 2. Travel Buffer Filter: Parse full exact time to make sure it's not starting right now
        full_appt_datetime = datetime.strptime(clean_timestamp_str, "%m/%d/%Y %I:%M %p")
        
        # Define minimum threshold (Now + 60 minutes)
        min_travel_cutoff = datetime.now() + timedelta(minutes=60)
        
        if full_appt_datetime < min_travel_cutoff:
            logging.info(f"⚠️ Skipping slot at {clean_timestamp_str} - too short notice to travel (under 60 min away).")
            return False, clean_timestamp_str

        return is_sooner, clean_timestamp_str
    except Exception as e:
        logging.error(f"Error parsing date/time layout matching '{calendar_text}': {e}")
        return False, None
    
def run_dmv_sweep():
    # Quiet hours check: Don't run between 1AM and 9AM to match human sleep patterns
    current_hour = datetime.now().hour
    if 1 <= current_hour < 9:
        logging.info("DMV system is outside standard waking hours (1 AM - 9 AM). Skipping sweep.")
        return
    
    logging.info("Starting safe sequential sweep of target DMV locations...")

    with sync_playwright() as p:
        # Launching browser constrained to standard laptop frame scaling boundaries
        browser = p.firefox.launch(headless=True, args=["--start-maximized"])
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0", 
            viewport={"width": 1280, "height": 720}, 
            locale="en-US"
        )

        page = context.new_page()
        page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        try:
            page.goto(START_URL, wait_until="networkidle")
            human_delay(2.5, 4.5)

            for loc in LOCATIONS:
                logging.info(f"Checking location: {loc}")

                # Step 1: Click the target location from the main index list
                page.get_by_text(loc, exact=False).first.click()
                human_delay(1.5, 3.0)

                # Step 2: Click the renewal service item button
                page.get_by_text("Renew Colorado Driver License/ID/Permit").click()
                human_delay(2.0, 4.0)

                ## If you want to search for something other than this appointment type, 
                ## Change the text in quotes to "CDL Written Test", "First Time CO DL/ID/Permit", 
                ## or "Written Test" (for CO DMVs only, other states will likely be different).

                # Step 3: Inspect page layout content string data
                raw_text = page.locator("body").text_content()
                lines = [line.strip() for line in raw_text.split("\n") if "/" in line and "2026" in line]
                target_string = lines[0] if lines else ""

                # Evaluate slot metrics while preserving full timestamp layout
                is_sooner, full_appointment_details = parse_and_validate_date(target_string)
                
                # Automatically save telemetry data row to tracking sheet cache
                log_data_point(loc, full_appointment_details)

                if is_sooner:
                    # Executes raw ASCII system bell sequence to trigger terminal audio alerts
                    logging.info(f"\a\a\a\U0001F6A8\U0001F6A8\U0001F6A8 MATCH FOUND AT {loc}! \U0001F6A8\U0001F6A8\U0001F6A8\n\U0001F6A8\U0001F6A8\U0001F6A8 Open Date/Time: {full_appointment_details} \U0001F6A8\U0001F6A8\U0001F6A8")
                    send_discord_alert(loc, full_appointment_details)
                else:
                    logging.info(f"Checked {loc}. Earliest slot: {full_appointment_details or 'None displayed'}")

                # Step 4: Hit 'Back' out of the calendar view
                page.get_by_text("Back").click()
                human_delay(1.0, 2.5)

                # Step 5: Hit 'Back' out of the services selection to restore main index menu
                page.get_by_text("Back").click()
                human_delay(1.5, 3.0)

        except Exception as e:
            logging.error(f"Sweep error encountered: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    init_csv_ledger()
    while True:
        run_dmv_sweep()

        # Staggered loop rest: Choose random delay between 12 and 22 minutes
        sleep_seconds = random.randint(12 * 60, 22 * 60)
        logging.info(f"Sweep complete. Resting for {round(sleep_seconds / 60, 1)} minutes...")
        time.sleep(sleep_seconds)