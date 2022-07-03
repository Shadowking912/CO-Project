import sys
def takeInput():
    d=sys.stdin.readlines()
    instructions=[]
    index=[]
    h=0
    v=0
    for i in range(len(d)):
        if (d[i].split()!=[]):
            instructions.append(d[i].strip().split())
            if("".join(instructions[-1])[0:3]=="var"):
                v+=1
            index.append(i)
        if("hlt" in d[i]):
            if(i<len(d)-1):
                h=1
                print(f"Error at line no {i+1}: hlt not at end of program")
                exit(0)
            elif(h==1):
                print("More than one hlt")
                exit(0)
            else:
                h=1
    if(h==0):
        print("Error: missing hlt instruction")
        exit(0)
    i=0
    labels,variables=LABL(instructions,index,len(instructions),v)
    while i<len(instructions):
        if (instructions[i][0]=="var"):
            instructions.append(instructions.pop(0))
            index.append(index.pop(0))
        else:
            break
    return [instructions,labels,variables,index]