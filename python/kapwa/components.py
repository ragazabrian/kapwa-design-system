"""
Kapwa Design System - Python Component HTML Helpers
Generate accessible Kapwa HTML directly from Python backends (Flask, FastAPI, Django).
"""
from typing import Optional, List, Dict


def button(label: str, variant: str = "primary", size: str = "md", onclick: Optional[str] = None, custom_class: str = "") -> str:
    """Render a Kapwa pill button."""
    classes = f"kw-btn kw-btn--{variant}"
    if size != "md":
        classes += f" kw-btn--{size}"
    if custom_class:
        classes += f" {custom_class}"
    onclick_attr = f' onclick="{onclick}"' if onclick else ""
    return f'<button class="{classes}"{onclick_attr}>{label}</button>'


def card(title: str, content: str, subtitle: Optional[str] = None, footer: Optional[str] = None, interactive: bool = False) -> str:
    """Render a Kapwa rounded card."""
    card_class = "kw-card kw-card--interactive" if interactive else "kw-card"
    header_html = f'<div class="kw-card__header"><div><h3 class="kw-card__title">{title}</h3>'
    if subtitle:
        header_html += f'<p class="kw-card__subtitle">{subtitle}</p>'
    header_html += '</div></div>'
    
    footer_html = f'<div class="kw-card__footer">{footer}</div>' if footer else ""
    return f"""
    <div class="{card_class}">
      {header_html}
      <div class="kw-card__body">{content}</div>
      {footer_html}
    </div>
    """


def kpi_card(value: str, label: str, icon_name: str = "truck") -> str:
    """Render a KPI statistic metric card."""
    return f"""
    <div class="kw-kpi-card">
      <div class="kw-kpi-card__icon-wrapper">
        <svg class="kw-icon" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <use href="#icon-{icon_name}"></use>
        </svg>
      </div>
      <div>
        <div class="kw-kpi-card__value">{value}</div>
        <div class="kw-kpi-card__label">{label}</div>
      </div>
    </div>
    """


def chip(label: str, variant: str = "gate") -> str:
    """Render a Kapwa status chip (gate, late, approved)."""
    return f'<span class="kw-chip kw-chip--{variant}">{label}</span>'


def switch(checked: bool = False, id_name: Optional[str] = None, onchange: Optional[str] = None) -> str:
    """Render an iOS-style Kapwa toggle switch."""
    id_attr = f' id="{id_name}"' if id_name else ""
    checked_attr = " checked" if checked else ""
    onchange_attr = f' onchange="{onchange}"' if onchange else ""
    return f"""
    <label class="kw-switch">
      <input type="checkbox" role="switch"{id_attr}{checked_attr}{onchange_attr}>
      <div class="kw-switch__track">
        <div class="kw-switch__thumb"></div>
      </div>
    </label>
    """


def linear_progress(percent: int = 60) -> str:
    """Render a smooth Kapwa linear progress bar."""
    return f"""
    <div class="kw-progress-linear">
      <div class="kw-progress-linear__bar" style="width: {percent}%;"></div>
    </div>
    """


def tabbar(tabs: Optional[List[Dict[str, str]]] = None, active_index: int = 0) -> str:
    """Render floating pill tab bar."""
    return f'<kapwa-tabbar active-index="{active_index}"></kapwa-tabbar>'


def render_page(title: str, content: str, css_path: str = "/css/kapwa.css", js_path: str = "/js/kapwa.js") -> str:
    """Render a full HTML5 page boilerplate using Kapwa Design System."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="{css_path}">
  <script type="module" src="{js_path}"></script>
</head>
<body style="padding: 24px; max-width: 1200px; margin: 0 auto;">
  <header style="margin-bottom: 32px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <h1 class="kw-display-md">{title}</h1>
      <p class="kw-caption">Rendered via Python Kapwa Engine</p>
    </div>
    <div>
      <button class="kw-btn kw-btn--outline kw-btn--sm" onclick="KapwaTheme.toggle()">Toggle Theme</button>
    </div>
  </header>
  <main>
    {content}
  </main>
</body>
</html>"""
