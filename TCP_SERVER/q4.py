


# 4. Allow data to be retrieved:
# Command: "GET <key>"
# Expected response: "<value>"
# Errors:
# - if key not found (ie., not previously set): "!404"
# - if syntax error: "!400"

hm={}
chars=[]
co=True
while co==True:
    chars=input(">")
    co=chars
    if chars[:4]=="GET ":
        k=chars[4:].split(" ")
        #print(k,v
        if k not in hm:
            print("!404")
        else:
            print(hm[k])
    else:
        print("!400")



