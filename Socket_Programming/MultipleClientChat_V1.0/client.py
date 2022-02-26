
import socket
from threading import Thread

name=input("Enter your Good name:")
conn=socket.socket()

#server_ip=input("Enter server's IP given to you:")
server_ip='192.168.194.187'
print("Socket created.. Connecting You to Chat room Please wait(INTERNET MUST BE ON)....")

try:
    conn.connect((server_ip,9999))
except:
    print("Sorry You are not able to connect to server try again..")

print("MIRACLE! YOU ARE CONNECTED..")
conn.send(name.encode())


def receive():
    while True:
        try:
            msg=conn.recv(1024).decode('utf-8')
            print(msg)
        except:
            print("Error in Receiving msg")
            conn.close()
            break

def send():
    while True:
        send_msg=f'{name}:> { input("ME:>") }'
        conn.send(send_msg.encode('utf-8'))


receive_thread=Thread(target=receive)
receive_thread.start()

send_thread=Thread(target=send)
send_thread.start()

