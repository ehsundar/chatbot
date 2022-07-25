import time
import os
from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(id(self))
        time.sleep(5)
        if self.path != "/":
            self.send_response(404)
            content = "not found"
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
            return
        content = ",".join(os.listdir(os.getcwd()))
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content.encode("ascii"))

    def do_POST(self):
        self.send_response(201)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(9))

        self.wfile.write(b"POST-POST")


def main():
    server = HTTPServer(("localhost", 8000), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()



if __name__ == "__main__":
    main()
