from http.server import BaseHTTPRequestHandler, HTTPServer
import mimetypes
import os

class RangeRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.range = None
        if 'Range' in self.headers:
            self.range = self.headers['Range']

        if self.range:
            self.send_response(206)
            self.send_header('Content-type', mimetypes.guess_type(self.path)[0])
            self.send_header('Accept-Ranges', 'bytes')

            file_size = os.path.getsize('.' + self.path)
            start, end = self.parse_range(self.range, file_size)
            self.send_header('Content-Range', f'bytes {start}-{end}/{file_size}')
            self.send_header('Content-Length', str(end - start + 1))
        else:
            self.send_response(200)
            self.send_header('Content-type', mimetypes.guess_type(self.path)[0])
            self.send_header('Content-Length', str(os.path.getsize('.' + self.path)))

        self.end_headers()

        with open('.' + self.path, 'rb') as file:
            if self.range:
                file.seek(start)
                self.wfile.write(file.read(end - start + 1))
            else:
                self.wfile.write(file.read())

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', mimetypes.guess_type(self.path)[0])
        self.send_header('Content-Length', str(os.path.getsize('.' + self.path)))
        self.send_header('Last-Modified', self.date_time_string(os.path.getmtime('.' + self.path)))
        self.end_headers()

    def parse_range(self, range_header, file_size):
        start, end = range_header.replace('bytes=', '').split('-')
        start = int(start) if start else 0
        end = int(end) if end else file_size - 1
        return start, end

def run_server():
    server_address = ('', 80)
    httpd = HTTPServer(server_address, RangeRequestHandler)
    print('Starting httpd...')
    httpd.serve_forever()

run_server()
