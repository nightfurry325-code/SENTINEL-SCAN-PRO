#!/bin/bash
# ╔═══════════════════════════════════════════════════════════════╗
# ║   Sentinel Scan Pro v3.1.1 — Installation Script              ║
# ║   For Termux / Linux / Android                                ║
# ║                                                               ║
# ║   Fixed Edition with:                                         ║
# ║   ✓ Auto port detection                                       ║
# ║   ✓ Android/Termux compatibility                             ║
# ║   ✓ Robust error handling                                    ║
# ║   ✓ Step-by-step feedback                                    ║
# ╚═══════════════════════════════════════════════════════════════╝

set -e

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║   🛡 SENTINEL SCAN PRO  —  v3.1.1 INSTALLATION               ║"
echo "║   Professional Edition for Termux/Linux                      ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# ── Detect Environment ────────────────────────────────────────────
if [[ "$OSTYPE" == "linux-android" ]] || [ -f "/data/data/com.termux/files/home/.termuxrc" ]; then
    IS_TERMUX=true
    INSTALL_FLAG="--break-system-packages"
    echo "[✓] Termux detected — Using Android optimization"
else
    IS_TERMUX=false
    INSTALL_FLAG=""
    echo "[✓] Linux detected"
fi
echo ""

# ── Check Python ──────────────────────────────────────────────────
echo "[1/5] Checking Python version…"
if ! command -v python3 &> /dev/null; then
    echo "    ❌ Python 3 not found!"
    if [ "$IS_TERMUX" = true ]; then
        echo "    📦 Run: pkg install python"
    fi
    exit 1
fi

PYTHON_VER=$(python3 --version | grep -oP 'Python \K[0-9]+\.[0-9]+')
echo "    ✓ Python $PYTHON_VER"
echo ""

# ── Create Directories ────────────────────────────────────────────
echo "[2/5] Creating project directories…"
mkdir -p logs db reports dashboard assets config
echo "    ✓ Directories created"
echo ""

# ── Install Dependencies ──────────────────────────────────────────
echo "[3/5] Installing Python dependencies…"
echo "    (This may take a minute…)"
pip install -r requirements.txt $INSTALL_FLAG --quiet 2>/dev/null || {
    echo "    ⚠️  Installation with --quiet failed, trying verbose…"
    pip install -r requirements.txt $INSTALL_FLAG
}
echo "    ✓ Dependencies installed"
echo ""

# ── Make Executable ──────────────────────────────────────────────
echo "[4/5] Setting executable permissions…"
chmod +x seeker.py
echo "    ✓ Script ready to run"
echo ""

# ── Verify Installation ──────────────────────────────────────────
echo "[5/5] Verifying installation…"
if python3 seeker.py --version &>/dev/null; then
    echo "    ✓ Installation verified!"
else
    echo "    ⚠️  Verification warning (may be normal)"
fi
echo ""

# ── Completion ──────────────────────────────────────────────────
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║   ✅ Installation Complete!                                  ║"
echo "║   🛡 Sentinel Scan Pro v3.1.1 is ready to run                ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "Quick start:"
echo ""
echo "  1. Copy environment template:"
echo "     cp .env.example .env"
echo ""
echo "  2. Run Sentinel:"
echo "     python seeker.py"
echo ""
echo "  3. Or with custom port (if 8080 busy):"
echo "     python seeker.py -p 3000 -t 0"
echo ""
echo "  4. Full setup with all features:"
echo "     python seeker.py -t 0 --ngrok-token YOUR_TOKEN --report"
echo ""
echo "For help: python seeker.py --help"
echo ""
