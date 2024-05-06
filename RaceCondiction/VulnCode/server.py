import socket 
from router import Router

class Banner:

    HEADER = '\033[5m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    CHERRY_BLOSSOM = '\033[1;35m'

    def __init__(self):
        self.meowBanner()

    def meowBanner(self):
        
        content = "Welcome, MeowHttpServer. ^O^"
        contentColor = self.ENDC + self.CHERRY_BLOSSOM + content + self.ENDC + self.HEADER
        countLength = len(content)
        if countLength % 2 != 0:content = content + " "
        countLenth2 = countLength // 2
        spaceNum = 24 - countLenth2
        # print("Number of characters:", countLength)
        
        print(self.HEADER)
        print("#"*50)
        print("#"+" "*48+"#")
        print("#" + " "*spaceNum + contentColor+ " "*spaceNum + "#")
        print("#"+" "*48+"#")
        print("#"*50)
        print(self.ENDC)
        
        print(self.WARNING + "-> Author: Meowhecker\n" + self.ENDC)

def server():

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # Once Deamon stop -> release socket Port
    serverSocket.bind(('0.0.0.0', 80))
    serverSocket.listen(20)

    print("Server Start http://127.0.0.1:80")

    while 1:

        # Receive Connection From Client !
        clientSocket, addr = serverSocket.accept()
        print("Receive Connection from ", addr)
        
        # Handle Cleint request
        requestHandler(clientSocket)


    serverSocket.close()


def requestHandler(clientSocket):
    
    router = Router()

    #Receive Data from Client 
    clientTcpPayload = clientSocket.recv(1024).decode()
    clientRequestLines = clientTcpPayload.split('\r\n')

    #Extract Frist Line in HTTP Request
    clientRequestFristLine = clientRequestLines[0]
    print("Request Path = ",clientRequestFristLine)

    #Assign Method / PATH / Version 
    clientRequestMethod = clientRequestFristLine.split(' ')[0]
    clientRequestPath = clientRequestFristLine.split(' ')[1]
    clientRequestVersion = clientRequestFristLine.split(' ')[2]

    #Routing & Return HTML (Body)  
    httpPayload = router.route(clientRequestPath)
    payloadLength = len(httpPayload)

    # Construct Response Header
    httpHeader = (
    "HTTP/1.1 200 OK\r\n"
    f"Content-Length: {payloadLength}\r\n"
    "meowHeader: MeowHacker is a bad cat !!"
    "\r\n"
    )

    serverResponse = httpHeader + httpPayload

    clientSocket.sendall(serverResponse.encode())
    clientSocket.close()

banner=Banner()
server()