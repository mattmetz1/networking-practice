import socket

s = socket.socket()

port = 40674

s.connect(('127.0.0.1', port))

print("connected")

# receive data from the server
print(s.recv(1024))

s.close()
