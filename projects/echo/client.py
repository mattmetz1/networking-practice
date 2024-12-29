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
    # keep the connection open until we're done sending messages
    while True:

        # needs to be byte-like object
        MESSAGE = str.encode(input("Enter you're message: "))

        # when 'EXIT' is received break the loop
        if (MESSAGE.decode() == "EXIT"):
            s.send(MESSAGE)
            break

        # send of MESSAGE to server
        s.send(MESSAGE)

        # receive response
        print("Echoing:",s.recv(1024))

    # close the connection
    print("EXIT received, closing connection")
    s.close()

except socket.error as e:
    print("a socket error has occured:",e)
except Exception as e:
    print("a general error has occured",e)
