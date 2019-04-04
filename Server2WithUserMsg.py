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

""" First run  programme = Server2WithUSerMsg.py """
""" Then run Client2WithUserMsg.py """

print " -------- Programme eto receive input/text from client --------"
print "--- Chat between server2 and client 2---"

serverListeningSocket = socket.socket() # TCP/IP socket
serverHostname = 'localhost'
port = 5500

serverListeningSocket.bind((serverHostname, port))
serverListeningSocket.listen(1) # listening to only one client request
print "Server started to listening on ", port

(newlyCreatedSocketForClientHost, clientAddr) = serverListeningSocket.accept() # return value is a pair containing first one being a socket and 2nd is the address of the client
print "Received some connection from ", clientAddr
newlyCreatedSocketForClientHost.send("Sending Message to client (serv to clnt)  : Hello client")

data = newlyCreatedSocketForClientHost.recv(1024)
while data:
    print "Received data from Client :" , data
    msg = raw_input("Enter message or Exit:")
    if msg != 'EXIT':
        newlyCreatedSocketForClientHost.send(msg)
    else:
        break

    data = newlyCreatedSocketForClientHost.recv(1024)

newlyCreatedSocketForClientHost.close()
print "Client connection closed"

serverListeningSocket.close()
print "Server is shutdown"




