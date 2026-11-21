"""
Kapwa Design System - Python Package
A multi-platform design system for Web, Mobile, and Desktop in pure Python, HTML, CSS, and JavaScript.
"""

from .tokens import TOKENS, KapwaTokens
from .components import (
    button,
    card,
    kpi_card,
    chip,
    switch,
    tabbar,
    linear_progress,
    render_page
)
from .server import run_server

__version__ = "1.0.0"
__all__ = [
    "TOKENS",
    "KapwaTokens",
    "button",
    "card",
    "kpi_card",
    "chip",
    "switch",
    "tabbar",
    "linear_progress",
    "render_page",
    "run_server"
]
