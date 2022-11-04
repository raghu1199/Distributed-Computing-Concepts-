from distutils.cmd import Command


chars=[]
co=True
while co==True:
    chars=input(">")
    co=chars
    if chars[:5]=="echo ":
        ans="".join(chars[5:])
        print(ans)
    else:
        print("wrong")


