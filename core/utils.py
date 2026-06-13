#!/usr/bin/env python3
# core/utils.py — Utility functions

import socket
import platform
import psutil
from pathlib import Path

def find_free_port(start_port: int = 8080, max_attempts: int = 10) -> int:
    """Find available port (smart auto-detection for port conflicts)."""
    for offset in range(max_attempts):
        port = start_port + offset
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(("127.0.0.1", port))
            sock.close()
            return port
        except OSError:
            continue
    raise RuntimeError(f"No free port found after {max_attempts} attempts")

def get_system_info() -> dict:
    """Get system information (Android/Termux safe)."""
    return {
        "os": platform.system(),
        "platform": platform.platform(),
        "python": platform.python_version(),
        "cpu_count": psutil.cpu_count(),
        "total_memory": f"{psutil.virtual_memory().total / (1024**3):.1f} GB",
    }

def ensure_directories() -> None:
    """Create required directories."""
    dirs = ["logs", "db", "reports", "template"]
    for d in dirs:
        Path(d).mkdir(exist_ok=True)

def check_health() -> bool:
    """Health check - verify all systems operational."""
    try:
        ensure_directories()
        if Path("config.yaml").exists():
            import yaml
            with open("config.yaml") as f:
                yaml.safe_load(f)
        return True
    except Exception as e:
        print(f"Health check failed: {e}")
        return False
