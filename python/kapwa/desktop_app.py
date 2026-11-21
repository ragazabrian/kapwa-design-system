"""
Kapwa Design System - Desktop Application (Python Native GUI)
A native desktop GUI application utilizing Tkinter and styled with Kapwa Design System tokens.
Works out of the box on macOS, Windows, and Linux without any heavy webview dependencies!
"""
import tkinter as tk
from tkinter import ttk, messagebox
import json


class KapwaDesktopApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kapwa Design System · Construction Portal (Desktop)")
        self.geometry("980x720")
        self.minsize(800, 600)

        # Light / Dark state
        self.is_dark = False

        self.apply_theme()
        self.build_ui()

    def apply_theme(self):
        if self.is_dark:
            self.bg_canvas = "#090B10"
            self.bg_card = "#151821"
            self.fg_ink = "#F5F5F7"
            self.fg_slate = "#98989D"
            self.color_primary = "#0071E3"
            self.color_mist = "#1C1C1E"
            self.color_border = "#2A2D3A"
        else:
            self.bg_canvas = "#F2F4F8"
            self.bg_card = "#FFFFFF"
            self.fg_ink = "#1D1D1F"
            self.fg_slate = "#5F5F64"
            self.color_primary = "#0071E3"
            self.color_mist = "#F5F5F7"
            self.color_border = "#E5E7EB"

        self.configure(bg=self.bg_canvas)

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.apply_theme()
        # Refresh UI
        for widget in self.winfo_children():
            widget.destroy()
        self.build_ui()

    def build_ui(self):
        # Header Bar
        header = tk.Frame(self, bg=self.bg_card, height=72, padx=32, pady=16)
        header.pack(fill=tk.X, side=tk.TOP)

        title_label = tk.Label(
            header,
            text="Kapwa Design System",
            font=("Inter", 18, "bold"),
            bg=self.bg_card,
            fg=self.fg_ink
        )
        title_label.pack(side=tk.LEFT)

        subtitle_label = tk.Label(
            header,
            text="· Desktop Construction Portal",
            font=("Inter", 14),
            bg=self.bg_card,
            fg=self.fg_slate
        )
        subtitle_label.pack(side=tk.LEFT, padx=8)

        # Theme toggle button
        theme_btn_text = "☀ Light Mode" if self.is_dark else "☾ Dark Mode"
        theme_btn = tk.Button(
            header,
            text=theme_btn_text,
            command=self.toggle_theme,
            font=("Inter", 11, "bold"),
            bg=self.color_mist,
            fg=self.fg_ink,
            relief=tk.FLAT,
            padx=14,
            pady=6,
            cursor="hand2"
        )
        theme_btn.pack(side=tk.RIGHT)

        # Main Scrollable Content Container
        container = tk.Frame(self, bg=self.bg_canvas, padx=32, pady=24)
        container.pack(fill=tk.BOTH, expand=True)

        # 1. KPI Cards Row
        kpi_frame = tk.Frame(container, bg=self.bg_canvas)
        kpi_frame.pack(fill=tk.X, pady=(0, 20))

        self.create_kpi_card(kpi_frame, "10", "Arriving today", "🚚", 0)
        self.create_kpi_card(kpi_frame, "8", "Pending approvals", "⏱", 1)
        self.create_kpi_card(kpi_frame, "2", "At risk", "⚠", 2)

        # 2. Main Dual Panel (Left: Deliveries List, Right: Actions & Details)
        content_grid = tk.Frame(container, bg=self.bg_canvas)
        content_grid.pack(fill=tk.BOTH, expand=True)

        # Left Card: Deliveries
        left_card = tk.Frame(content_grid, bg=self.bg_card, padx=24, pady=24, relief=tk.FLAT, bd=0)
        left_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 12))

        tk.Label(left_card, text="Today's Deliveries", font=("Inter", 16, "bold"), bg=self.bg_card, fg=self.fg_ink).pack(anchor="w", pady=(0, 16))

        deliveries = [
            ("Chiller CH-3", "Today, 09:00", "Gate A", "#E8F3FF", "#0071E3"),
            ("Switchgear SWGR-1A", "Delayed 2 days", "Late", "#FEE2E2", "#D70015"),
            ("Fire alarm FACP-1", "Dock 2 · 08:00", "Approved", "#E8F5E9", "#2E7D32")
        ]

        for item, time_str, chip_label, chip_bg, chip_fg in deliveries:
            row = tk.Frame(left_card, bg=self.bg_card, pady=10)
            row.pack(fill=tk.X)

            info_subframe = tk.Frame(row, bg=self.bg_card)
            info_subframe.pack(side=tk.LEFT, fill=tk.X, expand=True)

            tk.Label(info_subframe, text=item, font=("Inter", 13, "bold"), bg=self.bg_card, fg=self.fg_ink).pack(anchor="w")
            tk.Label(info_subframe, text=time_str, font=("Inter", 11), bg=self.bg_card, fg=self.fg_slate).pack(anchor="w")

            chip = tk.Label(row, text=f"  {chip_label}  ", font=("Inter", 11, "bold"), bg=chip_bg, fg=chip_fg, pady=4)
            chip.pack(side=tk.RIGHT)

        # Divider
        tk.Frame(left_card, height=1, bg=self.color_border).pack(fill=tk.X, pady=16)

        # Actions inside left card
        action_row = tk.Frame(left_card, bg=self.bg_card)
        action_row.pack(fill=tk.X)

        btn_approve = tk.Button(
            action_row,
            text="Approve Selected",
            bg="#0071E3",
            fg="white",
            font=("Inter", 12, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.on_approve
        )
        btn_approve.pack(side=tk.LEFT, padx=(0, 8))

        btn_reject = tk.Button(
            action_row,
            text="Reject",
            bg="#D70015",
            fg="white",
            font=("Inter", 12, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.on_reject
        )
        btn_reject.pack(side=tk.LEFT)

        # Right Card: Crane window & Quick Actions
        right_card = tk.Frame(content_grid, bg=self.bg_card, padx=24, pady=24, relief=tk.FLAT)
        right_card.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(12, 0))

        tk.Label(right_card, text="TC-1 Crane Window", font=("Inter", 16, "bold"), bg=self.bg_card, fg=self.fg_ink).pack(anchor="w")
        tk.Label(right_card, text="Used 4h 10m of 6h · Steel L3 at 10:00", font=("Inter", 11), bg=self.bg_card, fg=self.fg_slate).pack(anchor="w", pady=(4, 16))

        # Progress Canvas
        progress_canvas = tk.Canvas(right_card, height=12, bg=self.color_mist, bd=0, highlightthickness=0)
        progress_canvas.pack(fill=tk.X, pady=(0, 20))
        progress_canvas.create_rectangle(0, 0, 300, 12, fill="#0071E3", outline="")

        # Quick Actions
        tk.Label(right_card, text="Quick Actions", font=("Inter", 14, "bold"), bg=self.bg_card, fg=self.fg_ink).pack(anchor="w", pady=(10, 8))

        actions = [
            ("📅 Schedule Lift", lambda: messagebox.showinfo("Kapwa Desktop", "Lift schedule window opened.")),
            ("📄 Scan Delivery Ticket", lambda: messagebox.showinfo("Kapwa Desktop", "Ticket scanning initiated.")),
            ("🔄 Reroute Gate", lambda: messagebox.showinfo("Kapwa Desktop", "Rerouting to Gate B."))
        ]

        for text, cmd in actions:
            btn = tk.Button(
                right_card,
                text=text,
                command=cmd,
                font=("Inter", 11),
                bg=self.color_mist,
                fg=self.fg_ink,
                relief=tk.FLAT,
                anchor="w",
                padx=16,
                pady=10,
                cursor="hand2"
            )
            btn.pack(fill=tk.X, pady=4)

    def create_kpi_card(self, parent, value, label, icon, col):
        card = tk.Frame(parent, bg=self.bg_card, padx=20, pady=16)
        card.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0 if col == 0 else 8, 0 if col == 2 else 8))

        tk.Label(card, text=icon, font=("Apple Color Emoji", 20), bg=self.bg_card).pack(anchor="w")
        tk.Label(card, text=value, font=("Inter", 26, "bold"), bg=self.bg_card, fg=self.fg_ink).pack(anchor="w", pady=(8, 0))
        tk.Label(card, text=label, font=("Inter", 11), bg=self.bg_card, fg=self.fg_slate).pack(anchor="w")

    def on_approve(self):
        messagebox.showinfo("Kapwa Design System", "Delivery for Chiller CH-3 confirmed and marked Approved.")

    def on_reject(self):
        messagebox.showwarning("Kapwa Design System", "Delivery rejected. Reason logged in audit registry.")


if __name__ == "__main__":
    app = KapwaDesktopApp()
    app.mainloop()
