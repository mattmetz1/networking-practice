import socket

# TCP Client

TCP_IP = '127.0.0.1'
TCP_PORT = 40674
BUFFER_SIZE = 1024

try:
    # create socket
    s = socket.socket()
    print("created socket")

except socket.error as e:
    print("error creating socket",e)

try:
    # connect
    s.connect((TCP_IP, TCP_PORT))
    print("connected")
except socket.error as e:
    print("error connecting",e)

try:
    # receive data from the server
    print("received from server:\n",s.recv(1024))

    s.close()

except socket.error as e:
    print("a socket error has occured:",e)
except Exception as e:
    print("a general error has occured",e)
