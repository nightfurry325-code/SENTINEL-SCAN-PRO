#!/usr/bin/env python3
# core/config.py — Smart configuration management

import os
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

DEFAULTS = {
    "port": None,  # Auto-detect
    "template": None,
    "telegram": None,
    "webhook": None,
    "kml": None,
    "no_tunnel": False,
    "ngrok_token": None,
    "dashboard": True,
    "dashboard_port": 5000,
    "report": False,
    "csv": False,
    "geofence": None,
    "debug": False,
}

class Config:
    """Priority: CLI > ENV > YAML > defaults"""

    def __init__(self, config_path: str = "config.yaml"):
        self._data = dict(DEFAULTS)
        if config_path and Path(config_path).exists():
            self._load_yaml(config_path)
        self._load_env()

    def _load_yaml(self, path: str):
        try:
            if yaml:
                with open(path) as f:
                    data = yaml.safe_load(f)
                if data:
                    self._data.update(data)
        except Exception:
            pass

    def _load_env(self):
        env_map = {
            "PORT": ("port", int),
            "TEMPLATE": ("template", int),
            "TELEGRAM": ("telegram", str),
            "WEBHOOK": ("webhook", str),
            "NGROK_TOKEN": ("ngrok_token", str),
            "KML": ("kml", str),
            "GEOFENCE": ("geofence", str),
        }
        for env_key, (attr, cast) in env_map.items():
            val = os.getenv(env_key)
            if val:
                try:
                    self._data[attr] = cast(val)
                except (ValueError, TypeError):
                    pass

    def merge_args(self, args):
        """Merge CLI arguments (override if explicitly set)."""
        if not args:
            return
        for key in DEFAULTS:
            val = getattr(args, key, None)
            if val is not None and val != DEFAULTS.get(key):
                self._data[key] = val

    def __getattr__(self, name: str):
        try:
            return self._data[name]
        except KeyError:
            raise AttributeError(f"Config has no attribute '{name}'")

    def __repr__(self):
        return f"<Config {self._data}>"
