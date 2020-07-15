#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Server socket TCP
"""

from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()

    message = connectionSocket.recv(1024)

    messageDecoded = message.decode()

    print("Message recieved: " + messageDecoded)

    modifiedMessage = messageDecoded.upper()

    connectionSocket.send(modifiedMessage.encode())

    connectionSocket.close()
