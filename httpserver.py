import http.server
import socketserver

PORT = 80
DIRECTORY = "htdocs"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at {}:{}".format(socketserver., PORT)
        httpd.serve_forever()


run_server()