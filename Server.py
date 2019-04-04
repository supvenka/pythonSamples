"""
----------------
Socket Server
----------------
Create a TCP/IP side using socket() function
Bind the socket with hostname and port using bind()
Listen for incoming conn using listen()
Accept the client connection using accept() : Waiting for the connection request to arrive
Send /receive the message to the client using send() and recv()
Disconn by closing the socket using close()

"""
# Here we are creating our own server
# Where ever you want to run the server  we will use this script
import socket
# create , bind, listen, accept, send/recv, close

serverListeningSocket = socket.socket() # TCP/IP socket
serverHostname = 'localhost'
port = 5500

serverListeningSocket.bind((serverHostname, port))
serverListeningSocket.listen(1) # listening to only one client request
print "Server started to listening on ", port

(newlyCreatedSocketForClientHost, clientAddr) = serverListeningSocket.accept() # return value is a pair containing first one being a socket and 2nd is the address of the client
print " Received some connection from ", clientAddr
newlyCreatedSocketForClientHost.send("Message from Server: Hello client")

newlyCreatedSocketForClientHost.close()
print "Client connection closed"

serverListeningSocket.close()
print "Server is shutdown"

# we need to first run Server prog
# then run client prog


