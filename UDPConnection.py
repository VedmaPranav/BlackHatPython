import socket

target_host = "127.0.0.1"
target_port = 443

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(b"AAARRRCCC",(target_host,target_port))
data, addr = client.recv(4096)
print(data)


