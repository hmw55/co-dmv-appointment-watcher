<h1 align=center>
    👀 CO DMV Appointment Watcher 👀 
</h1>

<p align=center>
    <strong>An automated local-first scraping pipeline built with Python  and Playwright.</strong><br>
    Monitors local Department of Motor Vehicles (DMV) appointment portals, builds an asynchronous data telemetry ledger, streams live visual telemetry to LibreOffice Calc dashboards, and triggers multi-channel Twilio SMS / terminal audio alerts the millisecond an early booking slot is detected.
</p>

<p align=center>
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python Version"><br>
    <img src="https://img.shields.io/badge/Playwright-Firefox-green?logo=playwright&logoColor=white" alt="Playwright Engine"><br>
    <img src="https://img.shields.io/badge/Twilio-SMS_Alerts-red?logo=twilio&logoColor=white" alt="Twilio Integration"><br>
    <img src="https://img.shields.io/badge/Analytics-LibreOffice_Calc-purple?logo=libreoffice&logoColor=white" alt="LibreOffice Integration">
</p>

---


## ⚡ Key Features ⚡

- **Anti-Fingerprint Automation:** Strips browser engine automation flags (`navigator.webdriver`) inline via JavaScript injections to bypass firewall telemetry checks. 
- **Human-Mimetic Execution:** Randomizes linear delay pacing arrays and schedules automated sleep parameters during standard late-night maintenance windows to isolate the host machine's IP reputation pool.
- **Unified Telemetry Recording:** Compiles multi-threaded diagnostic terminal events into a flat-text engine while generating a structured tracking matrix (`.csv`) ready for local ingestion.
- **Real-Time Data Mirroring:** Forwards incoming scheduling states into localized spreadsheet engines via persistent background file-pooling loops. 
- **Dual-Channel Alarm System:** Strikes synchronous hardware-level ASCII system bells (`\a`) directly within host machine emulator terminal screens while distributing instant Twilio SMS payloads to your phone.

> NOTE: This code is ONLY checking for an earlier date. It is NOT checking for an earlier time on the same date or any earlier date. If you would like to include looking for an earlier time on the same day, refer to `lines 17-30` in `dmv_bot.py`

> Additional Note: The bot will NOT notify for appointments within one hour of the current time. This choice was made due to the need for travel time. 

---

## 🛠️ Local Installation & Environment Verification 

### 1. Initialize the Runtime Environment
Clone this repository to your target location workstation directory, isolate your environment variables, and instantiate a localized Python virtual environment:

```bash
# Clone the codebase repository

## Via SSH
git@github.com:hmw55/co-dmv-appointment-watcher.git

## OR via HTTPS
https://github.com/hmw55/co-dmv-appointment-watcher.git

# Once cloned, cd into the repository
cd co-dmv-watcher

# Instantiate a localized virtual environment context

## Windows
python -m venv venv 

## Mac/Linux
python3 -m venv venv

# Activate the runtime execution environment context

## On Windows PowerShell:
.\venv\Scripts\Activate.ps1

## On Mac/Linux terminal:
source venv/bin/activate
```

### 2. Provision Native Dependencies
Install core scripting packages and invoke Playwright's isolated binary engine manager to pull down the customized security-patched Firefox browser footprint:

```bash
pip install -r requirements.txt
playwright install firefox
```

If for some reason the `requirements.txt` doesn't install or you want to do it yourself:

```bash
pip install playwright python-dotenv twilio
# Then
playwright install firefox
```

### 3. Bind Private Environment Secrets
Construct a local `.env` secure configuration text file matching your repository root directory and populate your exact credential parameters. 

```code
TWILIO_ACCOUNT_SID="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
TWILIO_AUTH_TOKEN="your_hexadecimal_twilio_auth_token"
TWILIO_PHONE_NUMBER="+1XXXXXXXXXX"
CELL_NUMBER="+1XXXXXXXXXX"
```

> Note: Ensure all target telecom telephone string values comply strictly with global E.164 translation layouts (e.g., prefixing your standard country identifier, such as `+1` for North American network nodes).

<details>
<summary style="font-size:1.4rem; font-weight:700;">👀 How to set up your Twilio SMS Gateway</summary>

<br>

Don't panic if you don't have a Twilio account yet — setting up a free sandbox trail takes less than 5 minutes and gives you plenty of free credits to run this alert pipeline. 

1. **Create an Account:** Head over to [Twilio](https://www.twilio.com/) and sign up for a free trial account (no credit card required).
2. **Verify your Email and Personal Phone Number:** During the onboarding steps, verify the personal cell phone number you want to receive the alerts on. This binds your number to the `CELL_NUMBER` variable.
3. **Claim your Virtual Number:** Once you drop onto your Twilio Console Dashboard, look for **"Phone Numbers"** link. Click it and you will find the **"Buy Phone Number"** button, where you can use your free credits to get a number. Copy the absolute string generated (including the `+1`). This goes into your `TWILIO_PHONE_NUMBER` variable. 
4. **Extract Account Credentials:** On the dashboard, scroll down to find your **Account SID** and your hidden **Auth Token**.
5. **Update your `.env` File:** Copy those strings directly into your local `.env` file wrapper. 

> *Note: Free trial accounts can only send SMS payloads to numbers explicitly verified in your portal console settings. If you want to route alerts to a partner's phone too, make sure you add them under the "Verified Caller IDs" tab inside your Twilio Portal.*

</details>

---

## 🎯 Configuration & Customization Profile 🎯
To adjust scheduling logic bounds, locate the configuration segment mapped near the top of `dmv_bot.py`:

```python
# --- CONFIGURATION PROFILE ---
START_URL = "https://coloradoappt.cxmflow.com/Appointment/Index/d74f48b1-33a9-428c-acd1-d7d1bfc9555c"
MY_CURRENT_APPOINTMENT = datetime(2026, 6, 9)

LOCATIONS = [
    "Adams",
    "Aurora",
    "Centennial",
    "Denver NE",
    "Denver Regional Service Center",
    "Parker",
    "Westminster"
]
```

### 🏔️ For Colorado Forks

1. Update `MY_CURRENT_APPOINTMENT` to represent your existing confirmed scheduling slot. The bot will automatically ignore any parsed calendar dates that match or fall further back than this benchmark.
2. Edit the string elements inside the `LOCATIONS` array loop block to isolate specific administrative offices relative to your local county geographic borders. 
3. If you are looking for appointments other than Renewing a Colorado Driver's License/ID/Permit, refer to `lines 168-170` of `dmv_bot.py`

###  🇺🇸 For Out-of-State Adaptation
If your state's DMV operates on a completely different framework, you can adapt the core engine structure to your regional portals. 

1. **Target Portal Identification:** Analyze your regional booking pages. If your state's administration builds portals on top of standardized booking systems like **CXM Flow**, **FastTrack**, or **Q-Matic**, you can retain the majority of this repository's element selection architecture. 
2. **Selector Adjustments:** Swap out standard element target strings like `"Renew Colorado Driver License/ID/Permit"` inside the script's `page.get_by_text()` selectors to match your states agency's specific services UI phrasing. 
3. **Parse Regex Calibration:** If your local system renders scheduling data strings via unique grammatical layouts, modify the `parse_and_validate_date()` subroutines to properly slice text tokens into clean parameters matching standard `datetime.strptime()` string formats.  

---

## 🛡️ Network Security Optimization (NordVPN Integration) 🛡️

State administration portals closely monitor automated system behaviors and flag suspicious transaction traffic patterns originating from single, static IP blocks. To protect your home network connection pool, it is highly recommended to run this pipeline behind **NordVPN** or another VPN. 

```text
[Local Automation Engine] → [Global NordVPN Encrypted Tunnel] → [State Portal Firewalls]
  (Runs dmv_bot.py Loop)        (Rotates Regional Nodes)        (Sees Clean Home IP User)
```

### Configuration Profiles 

#### Method A: Global Native Routing (Recommended)

1. Launch your local desktop NordVPN client software application layer before initiating the scripting execution process. 
2. Formally lock your proxy target routing coordinates to a stable, localized **United States** edge hub server. 
3. Initiation execution (`python dmv_bot.py`). Playwright's isolated networking adapter interfaces will automatically snap onto your active system tunnel.

#### Method B: Programmable Interface Design 
For high-availability configurations, inject real-time system network interface rotation patterns directly into the processing flow using standard terminal hooks: 

```python
import subprocess

def cycle_vpn_interface():
    # Signals NordVPN CLI engine nodes to roll interface points on loop iteration cycles
    logging.info("Cycling localized NordVPN proxy connection arrays...")
    subprocess.run(["nordvpn", "connect", "United_States"], stdout=subprocess.DEVNULL)
```

---

## 📊 Live Spreadsheet Analytics (LibreOffice Calc Setup) 📊

> I'm just a nerd who likes to see trend, you do NOT have to worry about this. 

The automation module maintains an asynchronous database logging table inside a tracking flat file named `dmv_appointment_trends.csv` Follow these configuration steps to construct a live, auto-updating dashboard in LibreOffice Calc that visualized cancellation patterns over time. 

### Local Interface Setup 

1. **Generate Source Ledger:** Boot the bot terminal script execution instance through at least one operational loop pattern pass to auto-build your initial root file structure: `dmv_appointment_trends.csv`
2. **Establish External Resource Link:**
    - Instantiate a fresh LibreOffice Calc file sheet and save it as DMV_Dashboard.ods directly in your workspace folder. 
    - Navigate the top control option banner index to: **Sheet → Insert Sheet from File...**
    - Select your local `dmv_appointment_trends.csv` matrix. 
    - **Crucial:** In the option prompt dialog frame, make sure you check the **Link** confirmation toggle box. Set your structural text delimiter separator explicitly to **Comma**. Click **OK**.
3. **Activate Automated Background Polling Cycles:**
    - Select **Edit → Link to External Files...** from the window control index. 
    - Highlight your target linked CSV data file footprint path entry.
    - Look down toward the lower boundary panel controls, tick the **Update every** activation checkbox, and lock the internal refresh delay to **60 seconds**. Click **Modify** and close. 
4. **Deploy Color-Coded Cross-Location Analytical Visualizations:**
    - Select data table layout tracks (Columns A, B, and C).
    - Choose **Insert → Pivot Table...** using your *Current selection**. 
    - Drag your **Scan Timestamp** field handle into the **Rows** panel interface block.
    - Drag you **DMV Location** field handle into the **Columns** panel interface block. 
    - Drag your **Earliest Available Appointment Date** field handle into the center **Data Fields** panel box. Click **OK**.
    - Highlight your newly generated multi-dimensional pivot summary tables grid block and select **Insert → Chart...** to output a custom **Line Chart**

As your background automation script processes scheduling events, LibreOffice Calc will dynamically capture the fresh row lines, extend your trend graph tracks, and maintain a clear, color-coded visual overview of your target DMV booking lines without requiring a manual reload. 

---

## 🔒 Git Security Architecture (`.gitignore`)

To ensure that confidential telecommunication phone assets, API authorization tracking blocks, and localized raw spreadsheet datasets never accidentally get committed to your public repository history, the project uses a strict local file system gatekeeper framework. 

The `.gitignore` matrix is explicitly defined as follows: 

```text
# Real-Time Telemetry Tracking Output Layers
dmv_appointment_trends.csv
dmv_master_log.txt

# LibreOffice Calc Workspace Binaries
*.ods

# Generated Visualization Image Files
*.png

# Dynamic Execution Context Files & System Locks
.env
venv/
__pycache__/
*.pyc
.pytest_cache/
```

---

### 🚀 Verification Flight Checklist

Before executing the master loop sequence, double-check your local environment properties:

*   [ ] Run `python -c "import playwright; print('Playwright Ready')"` inside your terminal to confirm path installation mappings.
*   [ ] Make sure your `.env` contains no bare quote padding marks or missing plus sign parameters inside your telephony string variables.
*   [ ] Confirm your master `DMV_Dashboard.ods` file sits directly inside the same file directory layer where your `main.py` asset sits to ensure relative resource calls resolve smoothly.