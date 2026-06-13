#!/usr/bin/env python3
# core/banner.py — Beautiful terminal branding (Android/Termux safe)

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box

console = Console()

LOGO = r"""
  ███████╗███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗
  ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝
  ███████╗█████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗
  ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝
  ███████║███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗
  ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝
     ███████╗ ██████╗ █████╗ ███╗   ██╗    ██████╗ ██████╗  
     ██╔════╝██╔════╝██╔══██╗████╗  ██║    ██╔══██╗██╔══██╗
     ███████╗██║     ███████║██╔██╗ ██║    ██████╔╝██████╔╝
     ╚════██║██║     ██╔══██║██║╚██╗██║    ██╔═══╝ ██╔══██╗
     ███████║╚██████╗██║  ██║██║ ╚████║    ██║     ██║  ██║
     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝
      PRO
"""

def show_banner(version: str) -> None:
    """Display beautiful startup banner (safe for Android/Termux)."""
    try:
        logo_text = Text(LOGO, style="bold cyan", justify="center")
        
        tagline = Text.assemble(
            ("Advanced Geolocation & Device Intelligence Platform\n\n", "dim cyan"),
            ("🔹", "bold cyan"), (" Termux/Linux Edition  •  ", "dim white"),
            ("v" + version, "bold yellow"), ("\n", ""),
            ("🔹", "bold cyan"), (" Real-time Dashboard  •  ", "dim white"),
            ("Multi-source IP Recon  •  ", "dim white"),
            ("Geofence Alerts", "dim white"),
        )
        
        panel = Panel(
            Align.center(Text.assemble(logo_text, "\n\n", tagline)),
            border_style="bright_cyan",
            padding=(1, 2),
            box=box.DOUBLE_EDGE,
        )
        
        console.print(panel)
        console.print()
    except Exception as e:
        # Fallback for Android/Termux environments
        console.print(f"[cyan]🛡 SENTINEL SCAN PRO v{version}[/]")
        console.print("[dim cyan]Advanced Geolocation & Device Intelligence[/]\n")
