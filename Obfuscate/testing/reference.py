import socket

def handle_request(client_socket):
    request_data = client_socket.recv(1024).decode()

    # 解析 HTTP 请求
    request_lines = request_data.split('\r\n')
    request_line = request_lines[0]
    method, path, _ = request_line.split()

    # 构建响应
    response_body = f"Hello, you requested {path}"
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Length: {}\r\n"
        "\r\n"
        "{}".format(len(response_body), response_body)
    )

    # 发送响应
    client_socket.sendall(response.encode())

    # 关闭连接
    client_socket.close()

def run_server():
    # 创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 8080))
    server_socket.listen(5)

    print("Server started at http://127.0.0.1:8080")

    while True:
        # 接受连接
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # 处理请求
        handle_request(client_socket)

    # 关闭服务器套接字
    server_socket.close()

if __name__ == "__main__":
    run_server()