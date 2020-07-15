#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reciever socket UDP
"""

from socket import *

recieverPort = 65432
# Create the TCP socket
recieverSocket = socket(AF_INET, SOCK_DGRAM)
recieverSocket.bind(("", recieverPort))

print("Ready to receive\n")

try:
    while True:
        # Reset the stats
        lastSequence = False
        errCount = 0
        count = 0
        while True:
            # Recieve the Payload
            payload, clientAddress = recieverSocket.recvfrom(2048)
            # Decode the Payload
            payloadDecoded = payload.decode()
            # Split the Payload into an array
            payloadDecoded = payloadDecoded.split(";")

            if payloadDecoded[0] == "End":
                sent = payloadDecoded[1]
                print("Payload finished!")
                print(str(sent) + " packages sent by sender.")
                print(str(count) + " packages recieved.")
                print(str(errCount) + " sequence errors.\n")
                break;
            else:
                try:
                    sequence = int(payloadDecoded[0])
                    message = payloadDecoded[1]
                    count += 1
                except ValueError:
                    print("Sequence error, not the correct Payload format.")
                    break;
                except IndexError:
                    print("Message error, not the correct Payload format.")
                    break;

                if lastSequence and sequence != (lastSequence + 1):
                    errCount += 1
                    responseMessage = "\nSequence error:\nLast sequence nr: " + str(lastSequence) + "\nCurrent sequence nr: " + str(sequence) + "\n"
                    print(responseMessage)

                lastSequence = sequence
except KeyboardInterrupt:
    print("\nExiting...")
