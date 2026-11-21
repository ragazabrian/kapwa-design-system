#!/usr/bin/env python3
"""
Kapwa Design System - Root Server Launcher
Run with: python3 server.py
"""
import sys
from pathlib import Path

# Add python directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent / "python"))

from kapwa.server import run_server

if __name__ == "__main__":
    run_server()
