import socket

# TCP Server

TCP_IP = ''
TCP_PORT = 40674
BUFFER_SIZE = 1024
TIMEOUT = 60

def handle_client(c):

    # waits for message
    print("waiting for input")
    while True:
        MESSAGE = c.recv(1024)
        if (MESSAGE.decode() == "EXIT"):
            break
        c.send(MESSAGE)

    # close connection with client
    print("EXIT received, closing connection")
    c.close()
    


try:
    # create socket
    s = socket.socket()
    print("successfully created socket")
except socket.error as e:
    print("socket creation failed",e)

try:
    # now bind the port
    s.bind((TCP_IP,TCP_PORT))
    print("successfully bound socket to port:",TCP_PORT)

    # put socket into listen with max of 1 connection for now
    s.listen(1)
    # timeout socket in seconds defined by TIMEOUT
    s.settimeout(TIMEOUT)

    print(f"socket is now listening and will timeout in {TIMEOUT} seconds")

    # keep socket up until an error or interrupted
    while True:
        # accept connection with client
        c, addr = s.accept()
        print("connection started with",addr)

        # hanle connection
        handle_client(c)

except socket.error as e:
    print("a socket error has occured",e)
except Exception as e:
    print("a non-socket error has occured",e)
