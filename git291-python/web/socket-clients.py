import socket
import time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect(('localhost', 50007))
  while True:
    s.sendall(b'Hello')
    data = s.recv(1024)
    print(repr(data))
    time.sleep(2)