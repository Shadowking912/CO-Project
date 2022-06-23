def LABL(d):
    labels=dict()
    for i in d:
        if ":" in i:
            t=i.split(":")
            labels[t[0]]=
def takeinput():
    f=open("input.txt","r")
    d=f.readlines()
    LABL(d)
    d="".join(d)
    d=d.split("\n")
    global instructions
    instructions=[]
    print(d)
    for i in d:
        if i.split()!=[]:
            instructions.append(i.split())
    f.close()
def encoding():
    global opcode
    opcode={"add":"10000","sub":"10001","load":"10100","st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","rs":"11000","ls":"11001","xor":"11010","or":"11011","and":"11100","not":"11101","cmp":"1110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010","movim":"10010","movr":"10011"}