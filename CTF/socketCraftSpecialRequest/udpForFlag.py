#work
import socket

# Target Server
server_ip = '10.10.15.170'
server_port = 5000


source_port = 5000

def send_udp_request(message, server_ip, server_port, source_port):
    
    # Create UDP Socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    client_socket.bind(('', source_port))
    
    # Send Message to Target Server
    client_socket.sendto(message.encode(), (server_ip, server_port))
    
    print("UDP request sent successfully.")
        
    client_socket.close()

if __name__ == "__main__":
    message = "Meowhecker In"
    send_udp_request(message, server_ip, server_port, source_port)