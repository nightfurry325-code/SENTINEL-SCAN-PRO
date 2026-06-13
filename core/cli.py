#!/usr/bin/env python3
# core/cli.py — Argument parser with smart defaults

import argparse

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="sentinel-scan-pro",
        description="🛡 Sentinel Scan Pro v3.1.1 — Advanced Geolocation & Device Intelligence",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
╔══════════════════════════════════════════════════════════════════╗
║                     QUICK START EXAMPLES                         ║
╚══════════════════════════════════════════════════════════════════╝

  Interactive mode:
    python seeker.py

  Auto-select template:
    python seeker.py -t 0

  Custom port (if 8080 busy):
    python seeker.py -p 3000 -t 0

  Full setup with all features:
    python seeker.py -t 0 --ngrok-token YOUR_TOKEN --report -tg "BOT:CHAT_ID"

  Geofence alert (5km Jakarta):
    python seeker.py -t 0 --geofence "-6.2,106.8,5"
        """
    )

    srv = p.add_argument_group("🌐 Server")
    srv.add_argument("-p", "--port", type=int, default=None, help="Port (auto-detect if free)")
    srv.add_argument("-t", "--template", type=int, default=None, help="Template index")
    srv.add_argument("--dashboard", action="store_true", default=True, help="Enable dashboard")
    srv.add_argument("--dashboard-port", type=int, default=5000, help="Dashboard port")

    tun = p.add_argument_group("🌍 Tunnel")
    tun.add_argument("--no-tunnel", action="store_true", help="Disable ngrok")
    tun.add_argument("--ngrok-token", type=str, default=None, help="ngrok token")

    exp = p.add_argument_group("📊 Export")
    exp.add_argument("-k", "--kml", type=str, default=None, help="Export GPS to KML")
    exp.add_argument("--report", action="store_true", help="Auto HTML report")
    exp.add_argument("--csv", action="store_true", help="Export CSV")

    ntf = p.add_argument_group("🔔 Notifications")
    ntf.add_argument("-tg", "--telegram", type=str, default=None, help="BOT_TOKEN:CHAT_ID")
    ntf.add_argument("-wh", "--webhook", type=str, default=None, help="Webhook URL")

    geo = p.add_argument_group("📍 Geofence")
    geo.add_argument("--geofence", type=str, default=None, help="LAT,LON,RADIUS_KM")

    cfg = p.add_argument_group("⚙️  Config")
    cfg.add_argument("--config", type=str, default="config.yaml", help="Config file")
    cfg.add_argument("--debug", action="store_true", help="Debug mode")

    util = p.add_argument_group("🔧 Utility")
    util.add_argument("--update", action="store_true", help="Check updates")
    util.add_argument("-v", "--version", action="store_true", help="Version")
    util.add_argument("--health", action="store_true", help="Health check")

    return p
