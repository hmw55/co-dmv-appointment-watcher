<h1 align=center>
    👀 CO DMV Appointment Watcher 👀 
</h1>

<p align=center>
    <strong>An automated, local-first scraping pipeline built with Python and Playwright.</strong><br>
    Monitors regional Department of Motor Vehicles (DMV) appointment portals, builds a local data telemetry ledger, streams live visual tracking to LibreOffice Calc dashboards, and dispatches instant Discord markdown notifications + terminal alerts the millisecond an early booking slot opens up.
</p>

<p align=center>
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python Version"><br>
    <img src="https://img.shields.io/badge/Playwright-Firefox-green?logo=playwright&logoColor=white" alt="Playwright Engine"><br>
    <img src="https://img.shields.io/badge/Notifications-Discord_Webhook-5865F2?logo=discord&logoColor=white" alt="Discord Integration"><br>
    <img src="https://img.shields.io/badge/Analytics-LibreOffice_Calc-purple?logo=libreoffice&logoColor=white" alt="LibreOffice Integration">
</p>

---

## ⚡ Key Features ⚡

- **Carrier-Proof Notifications:** Bypasses restrictive carrier A2P 10DLC filtering blocks entirely by piping instant real-time alerts straight into a private Discord channel via standard webhooks.
- **Anti-Fingerprint Automation:** Strips browser engine automation flags (`navigator.webdriver`) inline via JavaScript injections to bypass portal firewall telemetry checks. 
- **Human-Mimetic Execution:** Randomizes linear delay pacing arrays and schedules automated sleep parameters during standard late-night maintenance windows (1 AM - 9 AM) to preserve the host machine's IP reputation pool.
- **Unified Telemetry Recording:** Compiles sequential sweep events into a flat-text engine while simultaneously generating a structured tracking matrix (`.csv`) ready for local ingestion.
- **Dual-Channel Alarm System:** Strikes synchronous hardware-level ASCII system bells (`\a`) directly within host machine emulator terminal screens while distributing instant `@everyone` Discord client pings to your desktop and phone.

> 💡 **NOTE:** This code is ONLY checking for an earlier date than your benchmark. It does not take time into consideration when evaluating date cutoffs. If you want the bot to check for *any* earlier day OR time slot on the day of the appointment, switch the parsing logic string to include the 24-hour timestamp formatting referenced in `dmv_bot.py`.

> 🚗 **TRAVEL BUFFER FILTER:** The bot automatically drops notification updates for appointment slots scheduled within 60 minutes of the active system runtime clock. This prevents the system from waking you up for short-notice cancellation openings you couldn't physically drive to in time.

---

## 🛠️ Local Installation & Environment Verification 

### 1. Initialize the Runtime Environment
Clone this repository to your target directory, isolate your environment variables, and instantiate a localized Python virtual environment:

```bash
# Clone the codebase repository
git clone [https://github.com/hmw55/co-dmv-appointment-watcher.git](https://github.com/hmw55/co-dmv-appointment-watcher.git)

# Once cloned, cd into the repository
cd co-dmv-appointment-watcher

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
Install the required application footprint packages and invoke Playwright's isolated binary manager to pull down the customized browser footprint:

```bash
pip install -r requirements.txt
playwright install firefox
```

If manually configuring packages step-by-step:

```bash
pip install playwright python-dotenv requests
playwright install firefox
```

### 3. Bind to Private Webhook Secrets
Construct a local `.env` secure configuration text file in your repository root directory and populate your targeted Discord webhook endpoint:

```
START_URL="https://coloradoappt.cxmflow.com/Appointment/Index/d74f48b1-33a9-428c-acd1-d7d1bfc9555c"
DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/YOUR_PRIVATE_GENERATED_WEBHOOK_STRING"
```

Discord webhooks are completely free, bypass cellular telecom spam blocks, and drop instant notification cards straight onto your phone or desktop.

1. **Open Discord:** Open your Discord client app and create a private personal server.
2. **Create a Channel:** Add a dedicated text channel named something like `#dmv-alerts`.
3. **Open Integrations Layout:** Click the **Gear Icon (⚙️)** right next to the channel name to enter Channel Settings, then navigate to the **Integrations** tab.
4. **Generate Webhook:** Click **Webhooks**, select **Create Webhook**, and click the **Copy Webhook URL** button. 
5. **Update your `.env` File:** Paste that absolute URL string directly into your local `.env` file target wrapper. 

---

## 🎯 Configuration & Customization Profile 🎯

To adjust scheduling logic bounds, locate the configuration segment mapped near the top of the `dmv_bot.py`:

```python
# --- CONFIGURATION PROFILE ---
START_URL = "[https://coloradoappt.cxmflow.com/Appointment/Index/d74f48b1-33a9-428c-acd1-d7d1bfc9555c](https://coloradoappt.cxmflow.com/Appointment/Index/d74f48b1-33a9-428c-acd1-d7d1bfc9555c)"
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

### For Colorado Forks 
1. Update `MY_CURRENT_APPOINTMENT` to represent your maximum date threshold (e.g., your fallback appointment). The script will systematically evaluate scheduling loops and fire alert payloads for slots found earlier than this calendar date.
2. Modify the elements inside the `LOCATIONS` array block to isolate specific administrative offices relative to your local county geographic lines.
3. If you need to search for appointment profiles other than standard license processing (e.g., *CDL Written Testing*), change the exact service match string. See lines 175-177 of `dmv_bot.py`.

### For Out-of-State Adaption
If your state's agency operates on a completely separate booking portal framework, you can easily adapt the core browser engine:

1. **Target Portal Identification:** Analyze your regional booking pages. If your state's administration builds portals on top of standardized flow systems like **CXM Flow**, **FastTrack**, or **Q-Matic**, you can retain the majority of this repository's element click paths.
2. **Selector Adjustments:** Swap out standard element target strings like `"Renew Colorado Driver License/ID/Permit"` inside the script's `page.get_by_text()` selectors to match your state agency's specific services UI phrasing.
3. **Parse Regex Calibration:** If your local system renders scheduling data strings via unique grammatical layouts, modify the subroutines inside `parse_and_validate_date()` to properly slice text tokens into clean parameters matching your local date structures.

---

## 🛡️ Network Security Optimization (NordVPN Integration) 🛡️

State administration portals closely monitor automated system behaviors and flag suspicious transaction traffic patterns originating from single, static IP blocks. To protect your home network connection pool from hitting temporary threshold blocks, it is highly recommended to run this pipeline behind a VPN.

```text
[Local Automation Engine] → [Global NordVPN Encrypted Tunnel] → [State Portal Firewalls]
  (Runs dmv_bot.py Loop)        (Rotates Regional Nodes)        (Sees Clean Home IP User)
```

### Configuration Profiles

#### Method A: Global Native Routing (Recommended)
1. Launch your local desktop NordVPN client application layer before initiating the scripting execution process.
2. Formally lock your proxy target routing coordinates to a stable, localized **United States** edge hub server.
3. Initiate execution (`python dmv_bot.py`). Playwright's isolated networking adapter interfaces will automatically snap onto your active system tunnel.

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

> *Note: This is entirely optional for data tracking enthusiasts who want to visualize historical cancellation trends over time!*

The automation module maintains an asynchronous database logging table inside a tracking flat file named `dmv_appointment_trends.csv`. Follow these configuration steps to construct a live, auto-updating dashboard in LibreOffice Calc that visualizes cancellation patterns over time.

### Local Interface Setup
Local Interface Setup
1. **Generate Source Ledger:** Boot the bot terminal script execution instance through at least one operational loop pattern pass to auto-build your initial root file structure: `dmv_appointment_trends.csv`
2. **Establish External Resource Link:**
    - Instantiate a fresh LibreOffice Calc file sheet and save it as `DMV_Dashboard.ods` directly in your workspace folder.
    - Navigate the top control option banner index to: **Sheet ➔ Insert** Sheet from File...
    - Select your local `dmv_appointment_trends.csv` matrix.
    - **Crucial:** In the option prompt dialog frame, make sure you check the Link confirmation toggle box. Set your structural text delimiter separator explicitly to **Comma**. Click **OK**.
3. **Activate Automated Background Polling Cycles:**
    - Select **Edit ➔ Link to External Files...** from the window control index.
    - Highlight your target linked CSV data file footprint path entry.
    - Look down toward the lower boundary panel controls, tick the **Update every activation** checkbox, and lock the internal refresh delay to **60 seconds**. Click **Modify** and close.
4. **Deploy Color-Coded Cross-Location Analytical Visualizations:**
    - Select your direct data rows on the primary sheet.
    - Choose **Insert ➔ Chart...** right next to your data block.
    - Pick **Line** from the left-side chart menu wizard layout, confirm **Data series in columns**, check **First row as label**, and click **Finish**.

As your background automation script processes scheduling events, LibreOffice Calc will dynamically capture the fresh row lines, extend your trend graph tracks, and maintain a clear, color-coded visual overview of your target DMV booking lines without requiring a manual reload.

---

## 🔒 Git Security Architecture (.gitignore) 🔒

To ensure that confidential integration webhooks, API authorization tracking blocks, and localized raw spreadsheet datasets never accidentally get committed to your public repository history, the project uses a strict local file system gatekeeper framework.

The .gitignore matrix is explicitly defined as follows:

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

## 🚀 Verification Flight Checklist 🚀
Before executing the master loop sequence, double-check your local environment properties:

- [ ] Run python -c "import playwright; print('Playwright Ready')" inside your terminal to confirm path installation mappings.
- [ ] Run pip show requests to ensure your HTTP communication dependencies are fully locked into your execution shell context.
- [ ] Confirm your master DMV_Dashboard.ods file sits directly inside the same file directory layer where your dmv_bot.py asset sits to ensure relative resource calls resolve smoothly.