import socket

sock=socket.socket()
sock.bind(("127.0.0.1", 10002))   # max port 65535
sock.listen()

conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode("utf8"))

conn.close()
sock.close()
