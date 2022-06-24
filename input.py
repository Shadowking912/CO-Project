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
    for i in instructions:
        if (i[0]=="var"):
            instructions.append(instructions.pop(0))
    f.close()
def encodeRegister():
    reg={"R0":"000", "R1":"001", "R2":"010", "R3":"011", "R4":"100","R5":"101", "R6":"110", "FLAGS":"111"}
    return reg