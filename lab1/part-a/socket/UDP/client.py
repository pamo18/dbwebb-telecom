#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Client socket UDP
"""

from socket import *

serverName = "pamoserver"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Enter your message:\n")

clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())
clientSocket.close()
