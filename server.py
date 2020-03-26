import time
import socket

with socket.socket() as sock:
    sock.bind(("", 10002))
    sock.listen()
    while True:
        #         time.sleep(4)
        conn, addr = sock.accept()

        conn.settimeout(3)  # timeout := None|0|gt 0
        with conn:
            while True:
                try:
                    data = conn.recv(1024)
                    print(len(data))
                except socket.timeout:
                    print("close connection by timeout")
                    break

                if not data:
                    break
                # print(data.decode("utf8"))