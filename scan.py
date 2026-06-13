#!/usr/bin/env python3
"""
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║       🛡 SENTINEL SCAN PRO  —  v3.1.1  (PRODUCTION GRADE)          ║
║                                                                    ║
║       Advanced Geolocation & Device Intelligence Platform         ║
║       Fixed • Enhanced • Professional • Termux-Ready              ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
"""

__version__ = "3.1.1"
__author__ = "Sentinel engine"
__status__ = "Production"

import sys
import os
from pathlib import Path

# ── Detect environment correctly (Android/Termux safe) ─────────────
BASE_DIR = Path(__file__).parent.absolute()
os.chdir(BASE_DIR)

# ── Python version check ──────────────────────────────────────────
if sys.version_info < (3, 10):
    print(f"❌ Python 3.10+ required. Current: {sys.version.split()[0]}")
    sys.exit(1)

# ── Dependency verification ───────────────────────────────────────
_DEPS = {
    "rich": "rich",
    "flask": "Flask",
    "flask_socketio": "Flask-SocketIO",
    "requests": "requests",
    "yaml": "PyYAML",
    "jinja2": "Jinja2",
    "qrcode": "qrcode",
}

_MISSING = []
for pkg_import, pkg_display in _DEPS.items():
    try:
        __import__(pkg_import)
    except ImportError:
        _MISSING.append(pkg_display)

if _MISSING:
    print(f"\n❌ Missing: {', '.join(_MISSING)}")
    print(f"📦 Install: pip install {' '.join(_MISSING)} --break-system-packages\n")
    sys.exit(1)

# ── Safe imports ──────────────────────────────────────────────────
from rich.console import Console
console = Console()

# ── Main entry ────────────────────────────────────────────────────
def main():
    """Main application entry point."""
    from core.cli import build_parser
    from core.app import ScannerApplication
    
    parser = build_parser()
    args = parser.parse_args()
    
    # Quick exits
    if args.version:
        console.print(f"[cyan]Sentinel Scan Pro[/] [bold white]v{__version__}[/]")
        sys.exit(0)
    
    if args.update:
        from core.updater import check_update
        check_update(__version__)
        sys.exit(0)
    
    # Run application
    try:
        app = ScannerApplication(args, __version__)
        app.run()
    except KeyboardInterrupt:
        console.print("\n[bold red][-][/] [cyan]Shutdown initiated.[/]\n")
        sys.exit(0)
    except Exception as e:
        console.print(f"[bold red]❌ Fatal error:[/] {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
