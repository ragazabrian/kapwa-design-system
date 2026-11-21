"""
Kapwa Design System - Design Tokens in Python
Recreated from Figma: Brian's Playground (Construction · Mobile component sheet)
"""
import json
from dataclasses import dataclass, asdict

TOKENS = {
    "colors": {
        "primary": "#0071e3",
        "primary_hover": "#0077ed",
        "primary_active": "#0062c4",
        "apple_blue": "#0066cc",
        "destructive": "#d70015",
        "destructive_hover": "#e01a2c",
        "warning": "#f59e0b",
        "success": "#34c759",
        "purple": "#5536d9",
        "purple_container": "#e2dcf2",
        "ink": "#1d1d1f",
        "slate": "#5f5f64",
        "hairline": "#d6d6d6",
        "studio_mist": "#f5f5f7",
        "control_gray": "#e6e6e8",
        "bg_canvas": "#f2f4f8",
        "surface_card": "#ffffff",
        "on_primary": "#ffffff"
    },
    "colors_dark": {
        "primary": "#0071e3",
        "ink": "#f5f5f7",
        "slate": "#98989d",
        "hairline": "rgba(255, 255, 255, 0.12)",
        "studio_mist": "#1c1c1e",
        "control_gray": "#38383a",
        "bg_canvas": "#090b10",
        "surface_card": "#151821"
    },
    "typography": {
        "display_large": {"size": "44px", "line_height": "1.15", "weight": 600, "tracking": "-1.1px"},
        "display_medium": {"size": "40px", "line_height": "1.15", "weight": 500, "tracking": "-1.0px"},
        "h1": {"size": "28px", "line_height": "34px", "weight": 600},
        "h2": {"size": "25px", "line_height": "31px", "weight": 600},
        "h3": {"size": "22px", "line_height": "28px", "weight": 600},
        "h4": {"size": "20px", "line_height": "26px", "weight": 600},
        "body_1": {"size": "16px", "line_height": "22px", "weight": 500},
        "body_2": {"size": "15px", "line_height": "21px", "weight": 500},
        "button": {"size": "15px", "line_height": "21px", "weight": 500},
        "caption": {"size": "13px", "line_height": "19px", "weight": 500}
    },
    "radii": {
        "card": "44px",
        "card_sm": "34px",
        "tile": "24px",
        "button": "9999px",
        "chip": "9999px"
    },
    "shadows": {
        "card": "0px 8px 28px 0px rgba(13, 18, 38, 0.05)",
        "button_primary": "0px 8px 12px rgba(13, 18, 38, 0.25)",
        "tabbar": "0px 14.4px 20.2px rgba(13, 18, 38, 0.1)",
        "active_tab": "0px 8.6px 20.2px 0px rgba(107, 77, 255, 0.45)"
    }
}


class KapwaTokens:
    """Helper class to access tokens programmatically in Python applications."""

    @classmethod
    def get_color(cls, name: str, dark: bool = False) -> str:
        palette = TOKENS["colors_dark"] if dark else TOKENS["colors"]
        return palette.get(name, TOKENS["colors"].get(name, "#000000"))

    @classmethod
    def to_json(cls, indent: int = 2) -> str:
        return json.dumps(TOKENS, indent=indent)

    @classmethod
    def to_css_variables(cls) -> str:
        lines = [":root {"]
        for k, v in TOKENS["colors"].items():
            lines.append(f"  --kw-color-{k.replace('_', '-')}: {v};")
        for k, v in TOKENS["radii"].items():
            lines.append(f"  --kw-radius-{k.replace('_', '-')}: {v};")
        lines.append("}")
        return "\n".join(lines)
