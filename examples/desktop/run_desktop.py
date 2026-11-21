#!/usr/bin/env python3
"""
Launcher for Kapwa Design System Desktop Application
Run with: python3 run_desktop.py
"""
import sys
import os
from pathlib import Path

# Add python directory to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "python"))

from kapwa.desktop_app import KapwaDesktopApp

if __name__ == "__main__":
    print("Launching Kapwa Design System Native Desktop Portal...")
    app = KapwaDesktopApp()
    app.mainloop()
