from wsgiref.simple_server import make_server

from app import application

if __name__ == '__main__':
    with make_server('', 8080, application) as httpd:
        print(" * Serving on http://{0}:{1} (Press CTRL+C to quit)"
              .format(*httpd.server_address))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
