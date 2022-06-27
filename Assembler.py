class stack:
    def __init__(self):
        self.data=[]
        
    def getSize(self):
        return len(self.data)

    def isEmpty(self):
        if len(self.data)>0:
            return False
        return True

    def push(self,data):
        self.data.append(data)

    def pop(self):
        if len(self.data)==0:
            return -1
        return self.data.pop()

    def top(self):
        return self.data[-1]


def LABL(d):
    labels=dict()
    variables=dict()
    for lineno in range(len(d)):
        if ":" in "".join(d[lineno]):
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
    for i in d:
        if (i.split()!=[]):
            instructions.append(i.strip().split())
     #labels dictionary
    i=0
    while i<len(instructions):
        if (instructions[i][0]=="var"):
            instructions.append(instructions.pop(0))
        else:
            break
   
    labels,variables=LABL(instructions)
    print(instructions)
    f.close()
    return [instructions,labels,variables]

def encoding():
    opcode={"add":"10000","sub":"10001","load":"10100","st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","rs":"11000","ls":"11001","xor":"11010","or":"11011","and":"11100","not":"11101","cmp":"1110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010","movim":"10010","movr":"10011"}
    return opcode
def encodeRegister():
    reg={"R0":"000", "R1":"001", "R2":"010", "R3":"011", "R4":"100","R5":"101", "R6":"110", "FLAGS":"111","r0":"000","r1":"001", "r2":"010", "r3":"011", "r4":"100","r5":"101", "r6":"110"}
    return reg
def findType():
    instructionType={"add":'A',"sub":'A',"mul":'A',"xor":'A',"or":'A',"and":'A','movim':'B',"ls":"B","movr":"C","div":"C","not":"C","cmp":"C","ld":"D","st":"D","jmp":"E","jlt":"E","jgt":"E","je":"E","hlt":"F"}
    return instructionType
def findUnused():
    unusedBits={'A':"00",'C':"00000","E":"000","F":"00000000000"}
    return unusedBits
def convert(immediateValue):
    immediateValue=int(immediateValue)
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
    for i in instructions:
        if i[0]=="var":
            break
        if i[0]=="mov":
            if i[2][0][0]=="$":
                i[0]+="im"
            else:
                i[0]+="r"
        encode=""
        encode+=opcode[i[0]]
        if instructionType[i[0]]=="A":
            encode+=unusedBits[instructionType[i[0]]]+reg[i[1]]+reg[i[2]]+reg[i[3]]
        elif instructionType[i[0]]=="B":
            immediateValue=i[2][1:]
            immediateValue=convert(immediateValue)
            encode+=reg[i[1]]+immediateValue
        elif instructionType[i[0]]=="C":
            encode+=unusedBits[instructionType[i[0]]]+reg[i[1]]+reg[i[2]]    
        elif instructionType[i[0]]=="D":
            memAddress=variables[i[2]]
            memAddress=convert(memAddress)
            encode+=reg[i[1]]+memAddress
        elif instructionType[i[0]]=="E":
            memAddress=labels[i[1]]
            memAddress=convert(memAddress)
            encode+=unusedBits[instructionType[i[0]]]+memAddress
        elif instructionType[i[0]]=="F":
            encode+=unusedBits[instructionType[i[0]]]
        encoded.append(encode)
    print(encoded)
main()