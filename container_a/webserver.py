#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import os
from typing import Final
from cgi import parse_header, parse_multipart
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler
import urllib.request


IC3000_ENV: Final = True
LISTEN_PORT: Final = 80
S1_ADDR: Final = '1.1.1.1'


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
        self.head = [
            '<head>',
            '<meta charset="utf-8">',
            '<title>s2</title>',
            '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">'
        ]

    def do_GET(self, last_cmd_output=None):
        log(last_cmd_output if last_cmd_output is not None else 'None')

        log(f'GET http://{S1_ADDR}')
        response = urllib.request.urlopen(f'http://{S1_ADDR}').read()
        log(f'Response: {response}')

        body = [
            '<div class="container">',
                '<h1 class="mx-auto">Reverse shell</h1>',

                f'<p>Request response: {response}</p>',
            '</div>'
        ]
        self._set_headers()
        self.wfile.write(bytes(
            f"<html>{''.join(self.head)}<body>{''.join(body)}</body></html>", 'utf8'
        ))


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
