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


instructions=[["add","R0","R1","R2"],["hlt"],["jlt","goto"],["mov","R2","$10"]]
# def findType():
instructionType={"add":'A',"sub":'A',"mul":'A',"xor":'A',"or":'A',"and":'A','movim':
    'B',"ls":"B","movr":"C","div":"C","not":"C","cmp":"C","ld":"D","st":"D","jmp":"E","jlt":"E","jgt":"E","je":"E","hlt":"F"}
    # return instructionType
unusedBits={'A':"00",'C':"00000","E":"000","F":"00000000000"}

reg={"R0":"000", "R1":"001", "R2":"010", "R3":"011", "R4":"100","R5":"101", "R6":"110", "FLAGS":"111"}
encoded=[]
opcode={"add":"10000","sub":"10001","load":"10100","st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","rs":"11000","ls":"11001","xor":"11010","or":"11011","and":"11100","not":"11101","cmp":"1110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010","movim":"10010","movr":"10011"}
variables={"X":"3"}
labels={"goto":"12"}
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
    # if instructionType[i[0]] in unusedBits:
    #     encode+=unusedBits[instructionType[i[0]]]
    if instructionType[i[0]]=="A":
        encode+=unusedBits[instructionType[i[0]]]+reg[i[1]]+reg[i[2]]+reg[i[3]]
    # Doubt ask about if immediate value is negative, how is it stored?
    elif instructionType[i[0]]=="B":
        immediateValue=i[2][1:]
        immediateValue=convert(immediateValue)
        # immediateValue=int(immediateValue)
        # immediateValue=bin(immediateValue)
        # immediateValue=str(immediateValue)
        # immediateValue=immediateValue[2:]
        # immediateValue=immediateValue[::-1]
        # bits=8-len(immediateValue)
        # j=1
        # while j<=bits:
        #     immediateValue+='0'
        #     j=j+1
        # immediateValue=immediateValue[::-1]
        encode+=reg[i[1]]+immediateValue
    elif instructionType[i[0]]=="C":
        encode+=unusedBits[instructionType[i[0]]]+reg[i[1]]+reg[i[2]]    
    elif instructionType[i[0]]=="D":
        memAddress=variables[i[2]]
        memAddress=convert(memAddress)
        # memAddress=int(memAddress)
        # memAddress=bin(memAddress)
        # memAddress=str(memAddress)
        # memAddress=memAddress[2:]
        # memAddress=memAddress[::-1]
        # bits=8-len(memAddress)
        # j=1
        # while j<=bits:
        #     memAddress+='0'
        #     j=j+1
        # memAddress=memAddress[::-1]
        encode+=reg[i[1]]+memAddress
    elif instructionType[i[0]]=="E":
        memAddress=labels[i[1]]
        memAddress=convert(memAddress)
        # memAddress=int(memAddress)
        # memAddress=bin(memAddress)
        # memAddress=str(memAddress)
        # memAddress=memAddress[2:]
        # memAddress=memAddress[::-1]
        # bits=8-len(memAddress)
        # j=1
        # while j<=bits:
        #     memAddress+='0'
        #     j=j+1
        # memAddress=memAddress[::-1]
        encode+=unusedBits[instructionType[i[0]]]+memAddress
    elif instructionType[i[0]]=="F":
        encode+=unusedBits[instructionType[i[0]]]
    encoded.append(encode)
for i in encoded:
    print(len(i))    
print(encoded)




        
