#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lab1b
Paul Moreland
pamo18
"""

from socket import *

host = "www.ingonline.nu"
query = "?board=xoxoeoeex"
target = "/tictactoe/index.php" + query
port = 80

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((host, port))

requestMessage = (
    "GET " + target + " HTTP/1.1\r\n" +
    "HOST: " + host + "\r\n" +
    "\r\n"
)

clientSocket.send(requestMessage.encode())

responseMessage = clientSocket.recv(1024)

# Print the response
print(responseMessage.decode())

# Close the connection
clientSocket.close()
