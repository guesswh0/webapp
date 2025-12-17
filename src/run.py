import signal
import sys
import time
from wsgiref.simple_server import make_server

from app import application


def _graceful_shutdown(signum, frame):
    time.sleep(10)  # simulate cleanup tasks
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, _graceful_shutdown)
    signal.signal(signal.SIGINT, _graceful_shutdown)

    with make_server('', 8080, application) as httpd:
        print(" * Serving on http://{0}:{1} (Press CTRL+C to quit)"
              .format(*httpd.server_address))
        try:
            httpd.serve_forever()
        finally:
            # Ensure clean shutdown
            print(" * Shutting down server...")
            httpd.server_close()
            print(" * Server shutdown complete")
