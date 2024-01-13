#!/bin python3
import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 9000))
serv.listen()

while True:
    conn, addr = serv.accept()
    print('Client from', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
    conn.close()
    print('Client disconnected')