from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import socket
import time
import os

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        

        #Configure Path
        root_directory = "./"
        path = self.path
        file_path = os.path.join(root_directory, path[1:])
        print(file_path)


       
        
        

        if os.path.exists(file_path):
            # 读取文件内容并发送回客户端
            with open(file_path, 'rb') as file:
                content = file.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content)
        else:
            # 文件不存在，返回 404 错误
            self.send_error(404, "File Not Found")

            
# request start 
#server.py->HTTPServer->socketserver->StreamRequestHandler->setup->_init_742
#
# reqeust finshed 
#server.py->HTTPServer->socketserver->StreamRequestHandler->finished->_init_742
#
if __name__ == '__main__':


    #server.py->HTTPServer->socketserver->StreamRequestHandler(785 line)
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    #print(httpd.socket)
    #print(httpd.server_name)
    print('Server started on port 8000...')
    httpd.serve_forever()
    