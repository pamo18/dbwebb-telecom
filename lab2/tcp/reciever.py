#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reciever socket TCP
"""

from socket import *

recieverPort = 65432
# Create the TCP socket
recieverSocket = socket(AF_INET, SOCK_STREAM)
recieverSocket.bind(('', recieverPort))
recieverSocket.listen(1)

print("Ready to receive\n")

try:
    while True:
        # Reset the stats
        lastSequence = False
        errCount = 0
        count = 0
        stream = ""
        # Open the connection
        connectionSocket, addr = recieverSocket.accept()

        while True:
            while True:
                payload = ""
                # Recieve the Payload
                data = connectionSocket.recv(1315)
                # Decode the Payload
                dataDecoded = data.decode()
                # Build the stream with frames
                stream += dataDecoded
                # Find a complete payload
                frameEnd = stream.find("#")

                if frameEnd != -1:
                    payload = stream[: frameEnd]
                    stream = stream[frameEnd + 1 :]
                    break;

            # Split the Payload into an array
            payloadDecoded = payload.split(";")

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
                    print("Sequence error, not the correct Payload format, restarting...")
                    break;
                except IndexError:
                    print("Message error, not the correct Payload format, restarting...")
                    break;

                if lastSequence and sequence != (lastSequence + 1):
                    errCount += 1
                    responseMessage = "\nSequence error:\nLast sequence nr: " + str(lastSequence) + "\nCurrent sequence nr: " + str(sequence) + "\n"
                    print(responseMessage)

                lastSequence = sequence
        # Close the current connection
        connectionSocket.close()
except KeyboardInterrupt:
    print("\nExiting...")
