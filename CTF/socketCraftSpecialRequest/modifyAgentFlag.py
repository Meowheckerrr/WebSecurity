#work
import socket

# Target Server
server_ip = '10.10.15.170'
server_port = 80



def send_udp_request(message, server_ip, server_port):
    
    # Create UDP Socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client_socket.connect((server_ip, server_port))
    
    # Send Message to Target Server
    client_socket.sendall(message.encode())
    
    print("TCP request sent successfully.")
        
    client_socket.close()

if __name__ == "__main__":
    message = "GET /fpassword.php?id=2 HTTP/1.\r\n User-Agent: I am Steve Friend\r\n\r\n"
    send_udp_request(message, server_ip, server_port)