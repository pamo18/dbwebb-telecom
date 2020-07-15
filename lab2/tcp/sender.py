#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sender socket TCP
"""

from socket import *
from random import randint
import time

recieverName = "192.168.1.212"
recieverPort = 65432

# Create the TCP socket
senderSocket = socket(AF_INET, SOCK_STREAM)
# Connect to the TCP socket
senderSocket.connect((recieverName, recieverPort))

# Ask user for setup details
t = input("Time to run in seconds?\n")
f = input("Messages per second?\n")
s = 1 / int(f)

sequenceError = input("Fake a random sequence error, y/n?\n")
sequence = 10000
message = 1300 * ("A")
count = 0

print("Sending...\n")
start = time.perf_counter()

while (time.perf_counter() - start) <= float(t):
    if sequenceError.lower() == "y" and randint(1, 10) == 1:
        sequence += 2
    else:
        sequence += 1

    # Create padding for equal size payloads
    padding = ""
    if len(str(sequence)) < 12:
        padding += (12 - len(str(sequence))) * ("0")

    # Create the Payload
    payload = str(sequence) + ";" + message + ";" + padding + "#"

    try:
        # Send the Payload
        senderSocket.send(payload.encode())
        # Update the counter
        count += 1
    except BrokenPipeError:
        print("Problem sending, is the payload correctly formatted?")
        break;

    # Wait before sending again
    time.sleep(s)

# Wait before sending final package to ensure it is last
time.sleep(5)

try:
    payloadEnd = "End;" + str(count) + ";#"
    # Send the Payload
    senderSocket.send(payloadEnd.encode())
    # Close the connection
    senderSocket.close()
    print("Payload finished!")
    print(str(count) + " packages sent.")
except BrokenPipeError:
    print("Connection closed, please try again.")
