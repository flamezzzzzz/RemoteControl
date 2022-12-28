import socket,threading


def func(sock):
    print(sock.recv(1024).decode())

server=socket.socket()
server.bind(('127.0.0.1', 5555))
server.listen()

while server:
    conn,add=server.accept()
    t=threading.Thread(target=func,args=(conn,))
    t.start()