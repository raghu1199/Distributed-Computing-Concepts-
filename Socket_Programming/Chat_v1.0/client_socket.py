import socket

# client socket 1)create sock 2) connect to server with ip+port 3) send data / recv data

conn=socket.socket()
conn.connect(('3.16.150.164',9999)) # server's public ip

name= input("Enter your name:")
conn.send(bytes(name,'utf-8'))  # send data

server_name=conn.recv(1024).decode()
print("connected with:",server_name)
print("*********WELCOME TO CHAT ROOM********** (created by Raghvendra Mishra)   ")
while True:
    recv_msg=conn.recv(1024).decode()
    print(server_name,":>",recv_msg)
    send_msg=input("Me:>")
    conn.send(send_msg.encode())
