# Kapwa Design System

<div align="center">

![Kapwa Design System](https://img.shields.io/badge/Kapwa-Design%20System-0071E3?style=for-the-badge&logo=materialdesign&logoColor=white)
![Multi-Platform](https://img.shields.io/badge/Platform-Web%20%7C%20Mobile%20%7C%20Desktop%20%7C%20Python-5536D9?style=for-the-badge)
![Zero TSX](https://img.shields.io/badge/TypeScript-None%20(Pure%20HTML%2FCSS%2FJS%2FPython)-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-CC0%201.0%20Universal-green?style=for-the-badge)

<p>
  <strong>An open-standard, multi-platform design system for Philippine public services, operations dashboards, and modern applications.</strong>
</p>
<p>
  Inspired by <a href="https://github.com/bettergovph/kapwa">bettergovph/kapwa</a> and crafted from the <a href="https://www.figma.com/design/T50WoEAytTKXBkpW5ERYLR/Brian-s-Playground?node-id=895-15020&t=hTmSXtKmq8nZvW3j-11">Figma Mobile Component Sheet</a>.
</p>

</div>

---

## 🌟 Why This Project?

While [bettergovph/kapwa](https://github.com/bettergovph/kapwa) provides a React/TypeScript/Tailwind implementation for web frameworks, many government agencies, enterprise portals, embedded systems, and desktop utilities rely on:
- **Clean HTML & CSS** without build pipelines or complex bundlers
- **Standard Vanilla JavaScript** & Web Components that run anywhere
- **Python backends** (Django, Flask, FastAPI) and **Native Python Desktop Apps** (Tkinter)
- **Responsive Mobile Applications** with iOS-feel tactile controls and bottom floating tab docks

**Kapwa Design System** delivers the exact visual fidelity and accessibility of the modern Filipino design language using standard web technologies and Python — **zero TSX, zero TypeScript compilation**.

---

## 🎨 Visual Target & Design Spec

Based on the [Brix Playground Design Sheet (Figma Node 895:15020)](https://www.figma.com/design/T50WoEAytTKXBkpW5ERYLR/Brian-s-Playground?node-id=895-15020&t=hTmSXtKmq8nZvW3j-11):

- **Brand & Pricing Blue**: `#0071E3` (Primary interactive pill, focus ring, active indicators)
- **Interactive Link Blue**: `#0066CC`
- **Risk Red**: `#D70015` (Destructive actions and late deliveries)
- **Primary Purple & Container**: `#5536D9` & `#E2DCF2` (Step indicators, accents)
- **Ink & Slate**: `#1D1D1F` (Light text) & `#5F5F64` (Muted labels)
- **Dark Mode**: `#090B10` canvas, `#151821` cards, `#F5F5F7` text
- **Radii**: `44px` cards, `9999px` pill buttons, `32px` tab indicators
- **Elevation**: Frosted glassmorphism (`backdrop-filter: blur(23px)`), soft shadows

---

## 📁 Repository Structure

```
kapwa-design-system/
├── css/                          # CSS Custom Properties & Component Styles
│   ├── tokens.css                # Color, typography, spacing, and shadow tokens (Light + Dark)
│   ├── reset.css                 # Modern base reset & accessible defaults
│   ├── typography.css            # Headings (H1-H4), Display, Body, and Caption styles
│   ├── buttons.css               # Pill, Outline Glass, Ghost, and Destructive buttons
│   ├── controls.css              # Switches, Checkboxes, and Radio buttons
│   ├── cards.css                 # Rounded 44px cards with elevation
│   ├── tabs.css                  # Floating frosted glass tab bar with sliding pill
│   ├── chips.css                 # Status chips (Gate A, Late, Approved, Filters)
│   ├── kpi.css                   # KPI statistic cards & counter badges
│   ├── charts.css                # Deliveries bar chart, donut chart, progress meters
│   ├── sheet.css                 # Confirm delivery modal sheet & drawers
│   └── kapwa.css                 # Master bundle stylesheet
│
├── js/                           # Zero-dependency Vanilla JS & Web Components
│   ├── kapwa.js                  # Master library entry point & dialog manager
│   ├── components/               # Custom Elements (<kapwa-button>, <kapwa-switch>, <kapwa-tabbar>)
│   └── utils/                    # Theme manager (Light/Dark) & SVG Icon library
│
├── python/                       # Pure Python Package
│   ├── kapwa/
│   │   ├── tokens.py             # Design tokens exported as Python dataclasses & JSON
│   │   ├── components.py         # Python HTML renderers for Flask/FastAPI/Django
│   │   ├── server.py             # Lightweight HTTP preview server & REST API
│   │   └── desktop_app.py        # Native Desktop Application with Tkinter GUI
│   └── pyproject.toml            # Pip installable package metadata
│
├── examples/
│   ├── mobile/index.html         # 1:1 Mobile Component Sheet from Figma
│   ├── web/dashboard.html        # Responsive Operations & Supply Chain Portal
│   └── desktop/run_desktop.py    # Desktop Python launcher
│
├── index.html                    # Interactive Documentation Site & Component Playground
├── LICENSE                       # CC0 1.0 Universal (Public Domain)
└── README.md
```

---

## 🚀 Quickstart

### 1. Web & Static HTML

Include the Kapwa stylesheet and modern JavaScript module:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="css/kapwa.css">
  <script type="module" src="js/kapwa.js"></script>
</head>
<body>
  <!-- Pill Button -->
  <button class="kw-btn kw-btn--primary">Approve</button>
  <button class="kw-btn kw-btn--outline">Reschedule</button>

  <!-- Fluid Switch Web Component -->
  <kapwa-switch checked></kapwa-switch>

  <!-- Floating Pill Tab Bar -->
  <kapwa-tabbar active-index="0"></kapwa-tabbar>
</body>
</html>
```

### 2. Mobile Application View

Open `examples/mobile/index.html` in any browser or mobile simulator to test the exact Figma sheet layout:
- Toggle between Light & Dark themes
- Touch-friendly floating bottom dock
- Interactive delivery list with status chips (`Gate A`, `Delayed`, `Approved`)
- Delivery modal confirmation sheet

### 3. Native Desktop Application (Python GUI)

Run the desktop application out of the box using Python's built-in GUI engine (macOS, Windows, Linux):

```bash
python3 examples/desktop/run_desktop.py
```

Features:
- Live theme switching (Light / Dark)
- Metric KPI cards (`10 Arriving today`, `8 Pending approvals`, `2 At risk`)
- Deliveries list with action buttons and dialogs
- TC-1 Crane Lift progress visualization

### 4. Local Documentation & API Server

Start the zero-dependency Python server:

```bash
python3 -m kapwa.server
# Or: python3 python/kapwa/server.py
```

Visit `http://localhost:8080` to explore the interactive component playground and test API endpoints:
- `GET /api/stats`
- `GET /api/deliveries`

---

## 🧩 Components Included

| Component | Figma Node | Description |
|-----------|------------|-------------|
| **Button Pill** | `895:15022` | Pill 47px height, Primary (`#0071E3`), Outline Glass, Ghost Link, Destructive (`#D70015`) |
| **Switch** | `895:15072` | iOS-style fluid pill toggle with 3:1 WCAG accessibility ratio |
| **Checkbox** | `895:15085` | Rounded square checkbox with checkmark and indeterminate dash |
| **Radio Button** | `895:15100` | Smooth radio disc with centered circular indicator |
| **Tab Bar** | `895:15132` | Frosted glass floating navigation with sliding active pill background |
| **KPI Card** | `895:15577` | 36px bold metric counter with icon container and description label |
| **Status Chip** | `895:15477` | Gate A (`#E8F3FF`), Late (`#FEE2E2`), Approved (`#E8F5E9`), Filter chips |
| **Bar Chart** | `895:15601` | Monthly deliveries bar chart with interactive time range selectors (1W-1Y) |
| **Progress Meters** | `897:15152` | Linear crane window progress (60%) & radial circular phase goals (100%, 62%) |
| **Confirm Sheet** | `895:15884` | Delivery confirmation modal sheet with supplier avatar, step indicator, and ticket row |

---

## 🤝 Filipino Design Values

1. **Malasakit (Compassion)**: User-first accessibility with high contrast ratios, readable font scales, and clean touch targets.
2. **Bayanihan (Communal Unity)**: Multi-platform interoperability so civic tech, web developers, and Python engineers can build cohesive tools together.
3. **Katapatan & Tiwala (Transparency & Trust)**: Clear states, audit indicators, and public domain licensing.

---

## 📄 License

This project is released under the **Creative Commons CC0 1.0 Universal** dedication. It is dedicated to the public domain and can be freely used by anyone for any purpose.
