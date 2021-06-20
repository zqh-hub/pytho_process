import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 我是8080，要向9090发消息
sk.bind(("192.168.0.103", 8080))
sk.sendto("你好！".encode("utf-8"), ("192.168.", 9090))
data = sk.recvfrom(1024)
print(data)
sk.close()
