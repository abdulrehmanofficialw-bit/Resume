import functools
import http.server
import socketserver
import threading
from pathlib import Path

import pytest

APP_DIR = Path(__file__).parent / "demo_app"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


@pytest.fixture(scope="session")
def demo_url():
    handler = functools.partial(QuietHandler, directory=str(APP_DIR))
    server = socketserver.TCPServer(("127.0.0.1", 0), handler)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    url = f"http://127.0.0.1:{server.server_address[1]}/index.html"
    yield url
    server.shutdown()
    server.server_close()
    server_thread.join(timeout=2)
