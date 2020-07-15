#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sender socket UDP
"""

from socket import *
from random import randint
import time

recieverName = "192.168.1.212"
recieverPort = 65432
# Create the TCP socket
senderSocket = socket(AF_INET, SOCK_DGRAM)
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

    # Create the Payload
    payload = str(sequence) + ";" + message

    # Send the Payload
    senderSocket.sendto(payload.encode(), (recieverName, recieverPort))

    # Update the counter
    count += 1

    # Wait before sending again
    time.sleep(s)

# Wait before sending final package to ensure it is last
time.sleep(5)

# Send message to close the reciever connection
payloadEnd = "End;" + str(count)
senderSocket.sendto(payloadEnd.encode(), (recieverName, recieverPort))

# Close the sender connection
senderSocket.close()

print("Payload finished!")
print(str(count) + " packages sent.")
