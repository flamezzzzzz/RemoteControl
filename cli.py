print("hi")
IP='127.0.0.1'
PORT=5555
import time
import pyautogui,socket

time.sleep(1)
sock=socket.socket()
sock.connect((IP,PORT))

while True:
     a = pyautogui.position()
     sock.send(str(a).encode())

     print('sent')


