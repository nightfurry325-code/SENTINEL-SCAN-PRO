#!/usr/bin/env python3
# core/app.py — ScannerApplication main orchestrator

import sys
from pathlib import Path
from rich.console import Console

console = Console()
BASE_DIR = Path(__file__).parent.parent

class ScannerApplication:
    """Main application coordinator."""

    def __init__(self, args, version: str):
        self.args = args
        self.version = version
        
        # Import core modules
        from core.config import Config
        from core.banner import show_banner
        from core.utils import find_free_port, ensure_directories
        
        # Health check
        ensure_directories()
        
        # Load configuration
        self.config = Config(args.config if hasattr(args, 'config') else "config.yaml")
        self.config.merge_args(args)
        
        # Display banner
        show_banner(version)
        
        # Smart port detection
        if self.config.port is None:
            try:
                self.config._data['port'] = find_free_port()
                console.print(f"[yellow][!] Port 8080 busy, using :{self.config.port}[/]\n")
            except RuntimeError:
                console.print("[bold red]❌ No available ports found![/]")
                sys.exit(1)

    def run(self):
        """Main application loop."""
        try:
            # Placeholder for full implementation
            console.print("[green][+][/] [cyan]Application running...[/]")
            console.print("[cyan]Template selection and scanning ready![/]")
        except KeyboardInterrupt:
            console.print("\n[bold red][-][/] [cyan]Shutdown.[/]\n")
        except Exception as e:
            console.print(f"[bold red]❌ Error:[/] {e}")
            if self.args.debug:
                import traceback
                traceback.print_exc()
