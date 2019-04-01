import socket

HOST = '127.0.0.9'
PORT = 65432
def sock:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print('Connected by', addr)
    data = s.recv(1024)
    print(data)

while True:
  sock
