#!/usr/bin/env python3
# core/db.py — SQLite database

import sqlite3
from pathlib import Path
from datetime import datetime
import json

class Database:
    """SQLite database for results."""

    def __init__(self, db_path: str):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_schema()

    def _connect(self):
        return sqlite3.connect(str(self.db_path))

    def _init_schema(self):
        """Create table if not exists."""
        schema = """
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            ip TEXT,
            os TEXT,
            platform TEXT,
            browser TEXT,
            lat TEXT,
            lon TEXT,
            acc TEXT,
            country TEXT,
            city TEXT,
            isp TEXT,
            risk_score INTEGER,
            risk_label TEXT,
            raw_json TEXT
        )
        """
        with self._connect() as con:
            con.execute(schema)
            con.commit()

    def save(self, record: dict) -> int:
        """Save record and return scan ID."""
        record = dict(record)
        record["timestamp"] = datetime.utcnow().isoformat()
        record["raw_json"] = json.dumps(record, default=str)
        
        record = {k: v for k, v in record.items() 
                  if isinstance(v, (str, int, float, bool, type(None)))}
        
        with self._connect() as con:
            cols = ", ".join(record.keys())
            placeholders = ", ".join("?" * len(record))
            cur = con.execute(
                f"INSERT INTO scans ({cols}) VALUES ({placeholders})",
                list(record.values())
            )
            con.commit()
            return cur.lastrowid

    def count(self) -> int:
        """Get total records."""
        with self._connect() as con:
            return con.execute("SELECT COUNT(*) FROM scans").fetchone()[0]
