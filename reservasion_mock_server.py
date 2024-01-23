# This is a mock server, do not use in production
import json
import random
import time
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer


class WebRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def get_response(self):
        rand_reservation_id = uuid.uuid4().hex

        content_length = int(self.headers.get('content-length', "0"))
        content = json.loads(self.rfile.read(content_length))

        self.log_message(f"req. content: {content}")

        req_params = "id"
        if content.get(req_params):
            data = {
                "status": "ok",
                "reservation_id": rand_reservation_id,
                "id": content["id"]
            }
        else:
            data = {
                "status": "error",
                "error_details": f"Missing req. parameter '{req_params}'"
            }
        return json.dumps(data)

    def do_POST(self):
        # artificial delay
        wait_seconds = random.randint(0, 30)
        self.log_message(f"Artificially waiting {wait_seconds} seconds")
        time.sleep(wait_seconds)

        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))


if __name__ == "__main__":
    conn_str = ("", 7999)
    print(f"Starting mock server: {conn_str[0]}:{conn_str[1]}")
    server = HTTPServer(conn_str, WebRequestHandler)
    server.serve_forever()
