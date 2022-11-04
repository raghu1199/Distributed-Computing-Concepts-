import socket

import errno


hm={}  # to store key value

server_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server socket created")

server_sock.bind(('0.0.0.0',1100))   # bind with server ip and particular port

server_sock.listen(20)
print("Waiting for connections...")


def echofunc(chars):
    co=chars
    if chars[:5]=="ECHO ":
        ans="".join(chars[5:])
        return ans
    else:
        return "500"

def setvalue(chars,hm):


    if chars[:4]=="SET ":
        k,v=chars[4:].split(" ")
        #print(k,v)
        hm[k]=v
        if k not in hm:
            return"!500"
        else:
            return "!200"
    else:
        return "!400"
    

def getvalue(chars,hm):

    if chars[:4]=="SET ":
        k,v=chars[4:].split(" ")
        #print(k,v)
        hm[k]=v
        if k not in hm:
            return"!404"
        else:
            return hm[k]
    else:
        return "!400"

def handleflush():
    return "-200"
def handle():
    return "200"




while True:
    try:
        client,addr = server_sock.accept()
        print("coonected to :",addr)
        while True:
            msg=""
            msg=client.recv(1024).decode() # recv data from client socke
            if msg[:5]=="ECHO ":
                ans=echofunc(msg)
                client.send(ans.encode())
            elif msg[:4]=="SET ":
                ans=setvalue(msg,hm)
                client.send(ans.encode())
            elif msg[:4]=="GET ":
                ans=getvalue(msg,hm)
                client.send(ans.encode())

            elif msg==" FLUSH ":
                ans=handleflush()
                client.send(ans.encode())

            else:
                ans=handle()
                client.send(ans.encode())
      
    except IOError as e:
        if e.errno == errno.EPIPE:
            pass


while True:
    client,addr = server_sock.accept()
    print("coonected to :",addr)
    while True:
        msg=""
        msg=client.recv(1024).decode() # recv data from client socke
        if msg[:5]=="ECHO ":
            ans=echofunc(msg)
            client.send(ans.encode())
        elif msg[:4]=="SET ":
            ans=setvalue(msg,hm)
            client.send(ans.encode())
        elif msg[:4]=="GET ":
            ans=getvalue(msg,hm)
            client.send(ans.encode())

        elif msg==" FLUSH ":
            ans=handleflush()
            client.send(ans.encode())

        else:
            ans=handle()
            client.send(ans.encode())


