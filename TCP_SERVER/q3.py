
# SET <key> <value>"
# Expected response: "!200"
# Errors:
# - if store is full: "!500"
# - if syntax error: "!400"
hm={}
chars=[]
co=True
while co==True:
    chars=input(">")
    co=chars
    if chars[:4]=="SET ":
        k,v=chars[4:].split(" ")
        #print(k,v)
        hm[k]=v
        if k not in hm:
            print("!500")
        
    else:
        print("!400")

