import socket

ip_address = ''
port = ''
buffer = ''
message = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_address, port))
s.send(message.encode())

s.close()

