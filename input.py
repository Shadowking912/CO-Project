def takeinput():
    f=open("input.txt","r")
    d=f.readlines()
    d="".join(d)
    d=d.split("\n")
    global instructions
    instructions=[]
    print(d)
    for i in d:
        if i.split()!=[]:
            instructions.append(i.split())
    f.close()