
import socket


# server socket 1) create sock (2) bind to server's ip and port (3) listen for connections
server_sock=socket.socket()
print("Server socket created")

server_sock.bind(('0.0.0.0',9999))   # bind with server ip and particular port

server_sock.listen(3)  # listen upto max 3 connection so 4th connection will be refused
print("Waiting for connections...")

while True:
    client,addr = server_sock.accept()
    name=client.recv(1024).decode() # recv data from client socket
    print("Connected with ",name,addr[0])
    
    client.send(bytes("Raghu",'utf-8'))  # send data to client using client socket objec
    
    while True:
        msg=input("ME:>")
        client.send(msg.encode())
        recv_msg=client.recv(1024).decode()
        print(name,":",recv_msg)


    client_sock.close()


server_sock.close()
