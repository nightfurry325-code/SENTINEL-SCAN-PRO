#!/usr/bin/env python3
# core/notifier.py — Multi-channel notifications

import requests
from rich.console import Console

console = Console()

class Notifier:
    """Send notifications via Telegram, Discord, Webhooks."""

    def __init__(self, telegram: str = None, webhook: str = None):
        self._tg = self._parse_telegram(telegram)
        self._wh = webhook

    def send(self, data: dict, msg_type: str):
        if self._tg:
            self._send_telegram(data, msg_type)
        if self._wh:
            self._send_webhook(data, msg_type)

    @staticmethod
    def _parse_telegram(val: str):
        if not val:
            return None
        parts = val.split(":")
        if len(parts) < 3:
            console.print("[yellow][!] Telegram format: BOT_TOKEN:CHAT_ID[/]")
            return None
        return parts

    def _send_telegram(self, data: dict, msg_type: str):
        try:
            p = self._tg
            token = f"{p[0]}:{p[1]}"
            chat_id = p[2]
            
            lines = [f"<b>🛡 Sentinel — {msg_type}</b>\n"]
            for k, v in data.items():
                if not str(k).startswith("_"):
                    lines.append(f"<b>{k}:</b> {v}")
            
            requests.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                json={"chat_id": chat_id, "text": "\n".join(lines), "parse_mode": "HTML"},
                timeout=8,
            )
        except Exception as e:
            console.print(f"[yellow][!] Telegram: {e}[/]")

    def _send_webhook(self, data: dict, msg_type: str):
        try:
            if "discord.com/api/webhooks" in self.._wh.lower():
                payload = self._discord_embed(data, msg_type)
            else:
                payload = data
            
            requests.post(self._wh, json=payload, timeout=8)
        except Exception as e:
            console.print(f"[yellow][!] Webhook: {e}[/]")

    @staticmethod
    def _discord_embed(data: dict, msg_type: str) -> dict:
        colors = {"device_info": 0x00CFFF, "ip_info": 0x3498DB, "location": 0x2ECC71}
        color = colors.get(msg_type, 0xAAAAAA)
        
        fields = [
            {"name": str(k), "value": str(v)[:1024], "inline": True}
            for k, v in data.items() if not str(k).startswith("_")
        ][:25]
        
        return {
            "embeds": [{
                "title": f"🛡 Sentinel — {msg_type}",
                "color": color,
                "fields": fields,
                "footer": {"text": "Sentinel Scan Pro v3.1.1"},
            }]
        }
