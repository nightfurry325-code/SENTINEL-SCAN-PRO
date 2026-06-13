#!/usr/bin/env python3
# core/updater.py — Update checker

import requests
from packaging import version
from rich.console import Console

console = Console()

def check_update(current: str):
    """Check for updates against GitHub metadata."""
    console.print("[cyan]Checking updates…[/]  ", end="")
    try:
        meta_url = "https://raw.githubusercontent.com/thewhiteh4t/seeker/master/metadata.json"
        r = requests.get(meta_url, timeout=5)
        if r.status_code == 200:
            console.print("[green]✔[/]")
            gh_ver = r.json().get("version", "0.0.0")
            if version.parse(gh_ver) > version.parse(current):
                console.print(f"[yellow][!] Update available: {gh_ver}[/]")
            else:
                console.print("[green][+] Already up to date[/]")
        else:
            console.print(f"[yellow]HTTP {r.status_code}[/]")
    except Exception as e:
        console.print(f"[yellow]Error: {e}[/]")
