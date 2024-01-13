import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class MyHandler(BaseHTTPRequestHandler):
    def handle(self):
        # 记录连接建立时间
        connection_start_time = time.time()
        
        # 处理其他请求...
        self.handle_one_request()

        # 记录连接结束时间
        connection_end_time = time.time()

        # 计算持续连接时间
        duration = connection_end_time - connection_start_time

        # 打印连接时间信息
        print(f"Connection from {self.client_address} started at {time.ctime(connection_start_time)} and ended at {time.ctime(connection_end_time)}")
        print(f"Duration of connection: {duration} seconds")

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print('Server started on port 8000...')
    httpd.serve_forever()