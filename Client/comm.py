import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    text = ""
    while True:
        try: data = s.recv(1024)
        except: break
        text += data.decode()
    with open("tmp.py", "w+") as f:
        f.write(text)
