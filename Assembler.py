# from sys import stdin
def LABL(d):
    labels=dict()
    variables=dict()
    for lineno in range(len(d)):
        if ":" in "".join(d[lineno]):
            if len(d[lineno])<2:
                print("Label does not start in the same line")
                # exit(0)
            else:
                t=" ".join(d[lineno]).split(":")
                d[lineno]=t[1].split()
                labels[t[0]]=str((lineno))
        elif "var" in d[lineno]:
            t="".join(d[lineno]).lstrip("var ")
            variables[t]=str((lineno))
    return [labels,variables]
def takeInput():
    f=open("input.txt","r")
    d=f.readlines()
    instructions=[]
    index=[]
    for i in d:
        if (i.split()!=[]):
            instructions.append(i.strip().split())
  
    i=0
    while i<len(instructions):
        if (instructions[i][0]=="var"):
            instructions.append(instructions.pop(0))
        else:
            break
    labels,variables=LABL(instructions)
    # print(instructions)
    f.close()
    return [instructions,labels,variables]

def encoding():
    opcode={"add":"10000","sub":"10001","load":"10100","st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","rs":"11000","ls":"11001","xor":"11010","or":"11011","and":"11100","not":"11101","cmp":"1110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010","movim":"10010","movr":"10011"}
    return opcode
def encodeRegister():
    reg={"R0":"000", "R1":"001", "R2":"010", "R3":"011", "R4":"100","R5":"101", "R6":"110","FLAGS":"111","r0":"000","r1":"001", "r2":"010", "r3":"011", "r4":"100","r5":"101", "r6":"110"}
    return reg
def findType():
    instructionType={"add":'A',"sub":'A',"mul":'A',"xor":'A',"or":'A',"and":'A','movim':'B',"ls":"B","movr":"C","div":"C","not":"C","cmp":"C","ld":"D","st":"D","jmp":"E","jlt":"E","jgt":"E","je":"E","hlt":"F"}
    return instructionType
def findUnused():
    unusedBits={'A':"00",'C':"00000","E":"000","F":"00000000000"}
    return unusedBits
def error(instruction):
    opcode=encoding()
    if instruction[0]=="var":
        return (f"Error variable not declared in starting at line no.")
    elif instruction[0] not in opcode:
        return (f"Error {instruction[0]} is not a valid operation.")
    elif (instruction[0]!="movr") and ("FLAGS" in instruction):
        return (f"Illegal use of flag register.")
    elif (instruction[0]=="movr") and (instruction[1]=="FLAGS"):
        return (f"Illegal use of flag register.")
    return "0"
def convert(immediateValue):
    immediateValue=int(immediateValue)
    if(immediateValue>511):
        return -1
    immediateValue=bin(immediateValue)
    immediateValue=str(immediateValue)
    immediateValue=immediateValue[2:]
    immediateValue=immediateValue[::-1]
    bits=8-len(immediateValue)
    j=1
    while j<=bits:
        immediateValue+='0' 
        j=j+1
    immediateValue=immediateValue[::-1]
    return immediateValue   
def main():
    opcode=encoding()
    unusedBits=findUnused()
    instructionType=findType()
    reg=encodeRegister()
    instructions,labels,variables=takeInput()
    encoded=[]
    print(instructions)
    for i in instructions:
        print(i)
        if i[0]=="mov":
            if i[2][0][0]=="$":
                i[0]+="im"
            elif i[2][0][0]=="R" or i[2][0][0]=="r":
                i[0]+="r"
            else:
                print(f"Invalid Syntax for {i[0]} instruction")
                exit(0)
        z=error(i)
        if(z!="0"):
            print(z)
            exit(0)
        encode=""
        encode+=opcode[i[0]]
        if instructionType[i[0]]=="A":
            if len(i)!=4:
                print(f"Invalid Syntax of instruction Type {i[0]}")
                exit(0)
            try:
                encode+=unusedBits[instructionType[i[0]]]+reg[i[1]]+reg[i[2]]+reg[i[3]]
            except Exception:
                print("The register is invalid.")
                exit(0)
        elif instructionType[i[0]]=="B":
            if len(i)!=3:
                print(f"Invalid Syntax of instruction Type {i[0]}")
                exit(0)
            try:
                immediateValue=i[2][1:]
                immediateValue=convert(immediateValue)
                if(immediateValue==-1):
                    print("The immediate value exceeds 8 bits")
                    exit(0)
                encode+=reg[i[1]]+immediateValue
            except Exception as e:
                print(f"The register {e} is invalid")   
                exit(0) 
        elif instructionType[i[0]]=="C":
            if len(i)!=3:
                print(f"Invalid Syntax of insruction Type {i[0]}")
                exit(0)
            try:
                encode+=unusedBits[instructionType[i[0]]]+reg[i[1]]+reg[i[2]]
            except Exception as e:
                print(f"The register {e} is invalid")
                exit(0)
        elif instructionType[i[0]]=="D":
            if(len(i)!=3):
                print(f"Invalid Syntax of instruction {i[0]}")
                exit(0)
            try:
                if(i[2] not in variables):
                    print(f"Variable {i[2]} not declared")
                    exit(0)
                memAddress=variables[i[2]]
                memAddress=convert(memAddress)
                encode+=reg[i[1]]+memAddress
            except Exception as e:
                print(f"The register {e} is invalid")
                exit(0)
        elif instructionType[i[0]]=="E":
            if(len(i))!=2:
                print(f"Invalid Syntax of instruction Type {i[0]}")
            try:
                if(i[1] not in labels):
                    print(f"Label {i[1]} does not exist")
                    exit(0)
                memAddress=labels[i[1]]
                memAddress=convert(memAddress)
                encode+=unusedBits[instructionType[i[0]]]+memAddress
            except Exception as e:
                print(f"The register {e} is invalid")
                exit(0)
        elif instructionType[i[0]]=="F":
            if(len(i)!=1):
                print(f"Invalid Syntax of instruction Type {i[0]}")
            encode+=unusedBits[instructionType[i[0]]]
        encoded.append(encode)
    print(encoded)
main()
