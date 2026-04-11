"""
Simple local server to run the Sales Analytics Dashboard.
Run this file, then open http://localhost:8000 in your browser.
"""
import http.server
import socketserver
import webbrowser
import threading
import os

PORT = 8000

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"  [{self.address_string()}] {format % args}")

def open_browser():
    import time
    time.sleep(0.8)
    webbrowser.open(f"http://localhost:{PORT}/dashboard.html")

print(f"\n  Sales Analytics Dashboard")
print(f"  --------------------------")
print(f"  Server running at: http://localhost:{PORT}/dashboard.html")
print(f"  Opening browser automatically...")
print(f"  Press Ctrl+C to stop.\n")

threading.Thread(target=open_browser, daemon=True).start()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
