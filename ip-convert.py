import socket
import struct

int_ip = 151723184
ip = socket.inet_ntoa(struct.pack('I', socket.htonl(int_ip)))
print(ip)