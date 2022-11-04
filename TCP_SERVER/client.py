import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.219.187',1100))
while True:
    send_msg=input("Me:>")
    sock.send(send_msg.encode())
    recv_msg=sock.recv(1024).decode()
    print(recv_msg)
    