#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Server socket UDP
"""

from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)

    messageDecoded = message.decode()

    print("Message recieved: " + messageDecoded)

    modifiedMessage = messageDecoded.upper()

    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
