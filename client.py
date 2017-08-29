import os
from socket import *
host = "192.168.2.40"
port = 13070
buf = 1024
addr = (host, port)
s = socket(AF_INET, SOCK_DGRAM)
s.bind(addr)
print "Waiting to receive messages..."
while True:
    (data, addr) = s.recvfrom(buf)
    print "Received message: " + data
    #str=int(raw_input("Client side message:"))
 #   data.send("Thank you for connecting")
    d = raw_input("Enter message to send or type 'exit': ")
    s.sendto(d, addr)

    if data == "exit":
        break
s.close()
os._exit(0)
