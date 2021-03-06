"""
----------------
Client Server
----------------
Create a TCP/IP side using socket() function
Connect the socket with the host name and port of the server using connect method
Send /receive the message to the client using send() and recv()
Disconn by closing the socket using close()

"""
# Here we are creating our own server
# Where ever you want to run the server  we will use this script
import socket
# create , connect,  send/recv, close

clientListeningSocket = socket.socket() # TCP/IP socket
serverHostnameIP = 'localhost'
serverPort = 5500

clientListeningSocket.connect((serverHostnameIP, serverPort))
print "Connection to the Server has been established ...."
dataRecivedFromServ = clientListeningSocket.recv(1024)

while dataRecivedFromServ:
    print "Data received from server = " , dataRecivedFromServ
    dataRecivedFromServ = clientListeningSocket.recv(1024)

clientListeningSocket.close()
print "Connection to the Server has been closed"

# we need to first run Server prog
# then run client prog