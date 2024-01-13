from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import time

class MyHandler(BaseHTTPRequestHandler):
    def setup(self):
        super().setup()
        self.connection_start_time = time.time()

    def handle(self):
        super().handle()

    def finish(self):
        super().finish()
        connection_end_time = time.time()
        duration = connection_end_time - self.connection_start_time
        print(f"Connection from {self.client_address} started at {time.ctime(self.connection_start_time)} and ended at {time.ctime(connection_end_time)}")
        print(f"Duration of connection: {duration} seconds")

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print('Server started on port 8000...')
    httpd.serve_forever()