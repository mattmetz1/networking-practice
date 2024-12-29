import socket

try:
    # create socket
    s = socket.socket()
    print("Socket created")

    # reserve port
    port = 40674

    # reserve ip
    ip = ''

    # now bind the port
    s.bind((ip,port))
    print("Successfully bound socket to port:",port)

    # put socket into listen with max of 1 connection for now
    s.listen(1)
    print("Socket is now listening")

    # keep socket up until an error or interrupted
    while True:
        # accept connection with client
        c, addr = s.accept()
        print ('Got connection from', addr )

        # send response to client
        c.send(b'Thank you for connecting')

        # close connection with cliet
        c.close()
except:
    print("An error has occured")
