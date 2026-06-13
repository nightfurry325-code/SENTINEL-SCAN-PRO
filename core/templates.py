#!/usr/bin/env python3
# core/templates.py — Template management system

import json
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()
BASE_DIR = Path(__file__).parent.parent

class TemplateManager:
    """Manage phishing templates."""

    def __init__(self):
        self.templates_file = BASE_DIR / "template" / "templates.json"
        self.templates = self._load_templates()

    def _load_templates(self) -> list:
        """Load templates from JSON config."""
        if not self.templates_file.exists():
            console.print(f"[yellow][!] templates.json not found[/]")
            return []
        
        try:
            with open(self.templates_file) as f:
                data = json.load(f)
            return data.get("templates", [])
        except json.JSONDecodeError:
            console.print("[yellow][!] Invalid templates.json[/]")
            return []

    def display(self) -> None:
        """Show template selection table."""
        if not self.templates:
            console.print("[red][-] No templates available[/]")
            return
        
        table = Table(
            title="[bold cyan]Available Templates[/]",
            box=box.ROUNDED,
            border_style="cyan",
            show_lines=True,
        )
        table.add_column("#", style="bold yellow", justify="center", width=3)
        table.add_column("Name", style="bold white")
        table.add_column("Description", style="dim white")
        
        for i, t in enumerate(self.templates):
            table.add_row(
                str(i),
                t.get("name", "Unknown"),
                t.get("description", "—"),
            )
        
        console.print(table)
        console.print()

    def get(self, index: int) -> dict | None:
        """Get template by index."""
        if 0 <= index < len(self.templates):
            return self.templates[index]
        return None

    def count(self) -> int:
        """Get total templates count."""
        return len(self.templates)
