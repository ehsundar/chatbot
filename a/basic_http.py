import time
from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # print(id(self))
        # time.sleep(10)
        if self.path != "/":
            self.send_response(404)
            content = "not found"
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
            return
        content = "Salam!"
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content.encode("ascii"))


def main():
    server = HTTPServer(("localhost", 8000), Handler)
    server.serve_forever()


if __name__ == "__main__":
    main()
