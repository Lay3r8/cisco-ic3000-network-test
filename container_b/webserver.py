#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from typing import Final
from http.server import BaseHTTPRequestHandler


IC3000_ENV: Final = True
LISTEN_PORT: Final = 80


def log(msg):
    print(msg)
    if IC3000_ENV:
        logf.write(f'{msg}\n')
        logf.flush()


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        log('GET')

        self._set_headers()
        self.wfile.write(json.dumps({'test': 'hello world'}).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, port=LISTEN_PORT):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    log(f'Python webserver listening on port {port}')
    httpd.serve_forever()


if __name__ == "__main__":
    if IC3000_ENV:
        log_file_dir = os.getenv("CAF_APP_LOG_DIR", "/tmp")
        log_file_path = os.path.join(log_file_dir, "webserver.log")
        logf = open(log_file_path, 'w')
    try:
        run()
    except KeyboardInterrupt:
        log('SIGINT received, shutting down server')
        if IC3000_ENV:
            logf.close()
        exit(0)
