from threading import Thread
import socket

server=socket.socket()
server.bind(("192.168.194.187",9999)) # if aws (public) server -> bind(("0.0.0.0",9999))
server.listen()

clients=[] #stores client socktes
names=[]

def broadcast(message):
    for client in clients:
        client.send(message)

# handle client function which recieves msgs from specific client in each separate thread, nd broadcast to all 
def handle_client(client):
    global clients
    global names
    while True:
        try:
            recv_msg=client.recv(1024)
            broadcast(recv_msg)

        except: # if not able to recv msg from specific client means that client is not connected 
            print("ERROR in handling client")
            index=clients.index(client)
            clients.pop(index)
            client.close()
            name=names[index]
            broadcast(f"{name} has left chat room...")
            names.remove(name)
            break 

# accept connection nd provide it to a separate thread for communication
def accept_connections():
    global clients
    global names
    while True:
        print("Server is listening for connections....")
        client,addr=server.accept()
        print(f"Connected to  ip: {addr[0]} port:{addr[1]}....")

        name=client.recv(1024).decode('utf-8')
        # print("name recvd:",name)
        
        #print(f"Afterv send recv Connected to  ip: {addr[0]} port:{addr[1]}....")

        clients.append(client)
        names.append(name)
        print("names:",names)
        
        broadcast(f"Attention! Great {name}  has joined the chat room...".encode('utf-8'))
        client.send("WELCOME TO CHAT ROOM".encode('utf-8'))

        thread=Thread(target=handle_client,args=(client,),daemon=True)
        thread.start()



accept_connections()
