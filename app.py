from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.respond(include_body=True)

    def do_HEAD(self):
        self.respond(include_body=False)

    def respond(self, include_body):
        path = urlsplit(self.path).path
        if path == "/health":
            status, body = 200, b'{"status":"ok"}\n'
        elif path == "/unhealthy":
            status, body = 503, b'{"status":"error"}\n'
        elif path == "/":
            status, body = 200, b'{"message":"Application is running"}\n'
        else:
            status, body = 404, b'{"status":"not_found"}\n'

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if include_body:
            self.wfile.write(body)


if __name__ == "__main__":
    print("Listening on 0.0.0.0:8080", flush=True)
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
