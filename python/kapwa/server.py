"""
Kapwa Design System - Local Preview Server & API
Run with: python3 -m kapwa.server
"""
import http.server
import socketserver
import os
import json
from pathlib import Path

PORT = 8080
BASE_DIR = Path(__file__).resolve().parent.parent.parent


class KapwaRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def do_GET(self):
        # Sample REST API endpoint
        if self.path == "/api/stats":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            data = {
                "arriving_today": 10,
                "pending_approvals": 8,
                "at_risk": 2,
                "total_deliveries": 142,
                "on_time": 118,
                "late": 24,
                "committed_value": "$18.4M"
            }
            self.wfile.write(json.dumps(data).encode("utf-8"))
            return

        elif self.path == "/api/deliveries":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            deliveries = [
                {"id": "CH-3", "name": "Chiller CH-3", "time": "Today, 09:00", "gate": "Gate A", "status": "gate"},
                {"id": "SWGR-1A", "name": "Switchgear SWGR-1A", "time": "Delayed 2 days", "gate": "Gate B", "status": "late"},
                {"id": "FACP-1", "name": "Fire alarm FACP-1", "time": "Dock 2 · 08:00", "gate": "Dock 2", "status": "approved"}
            ]
            self.wfile.write(json.dumps(deliveries).encode("utf-8"))
            return

        return super().do_GET()


def run_server(port=PORT):
    with socketserver.TCPServer(("", port), KapwaRequestHandler) as httpd:
        print(f"Kapwa Design System Preview Server running at: http://localhost:{port}")
        print(f"Serving files from: {BASE_DIR}")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")


if __name__ == "__main__":
    run_server()
