from vidstream import *
import tkinter as tk
from tkinter import *
import socket
import threading


ip_local = socket.gethostbyname(socket.gethostname())
#ip_public = requests.get('https://api.ipify.org').text
server1 = StreamingServer(ip_local, 9999)
#recv1 = AudioReceiver(ip_local, 8888)


def listening():
    thread1 = threading.Thread(target=server1.start_server)
    #thread2 = threading.Thread(target=recv1.start_server)
    thread1.start()
    #thread2.start()


def screen_share():
    client1 = ScreenShareClient(text_ip.get(1.0, 'end-1c'), 7777)
    thread3 = threading.Thread(target=client1.start_stream())
    thread3.start()

#gui
window = tk.Tk()
window.title("RemoteX")
window.geometry('500x500')


goal_ip = tk.Label(window, text="IP:")
goal_ip.pack()

text_ip = tk.Text(window, height=1)
text_ip.pack()

listen = tk.Button(window, text="Start Listening", width=25, command=listening)
listen.pack(anchor=tk.CENTER, expand=True)

screen = tk.Button(window, text="Start Screen Share", width=25, command=screen_share)
screen.pack(anchor=tk.CENTER, expand=True)


window.mainloop()










