class simulator:
    def __init__(self):
        self.opcode={"10000":"add","10001":"sub","10100":"ld","10101":"st","10110":"mul","10111":"div","11001":"ls","11000":"rs","11010":"xor","11011":"or","11100":"and","11101":"not","11110":"cmp","11111":"jmp","01100":"jlt","01101":"jgt","01111":"je","01010":"hlt","10010":"movim","10011":"movr"}
        self.reg={"000":"R0", "001":"R1", "010":"R2", "011":"R3", "100":"R4","101":"R5", "110":"R6","111":"FLAGS"}
        self.instructionType={"add":'A',"sub":'A',"mul":'A',"xor":'A',"or":'A',"and":'A','movim':'B',"rs":"B","ls":"B","movr":"C","div":"C","not":"C","cmp":"C","ld":"D","st":"D","jmp":"E","jlt":"E","jgt":"E","je":"E","hlt":"F"}
        self.unusedBits={'A':"00",'C':"00000","E":"000","F":"000000000"}
        self.instructions=[]
        self.regval={"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0,"FLAGS":['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']}
        self.pc=0
        self.getinput()
        
    def getinput(self):
        f=open("output.txt","r")
        self.instructions=f.readlines()
        self.instructions="".join(self.instructions)
        self.instructions=" ".join(self.instructions.split("\n"))
        self.instructions=self.instructions.split(" ")
        n=len(self.instructions)
        i=0
        while(i<n):
            if self.instructions[i][0:5]=="10110" or self.instructions[i][0:5]=="10101":
                self.instructions.append(0)
            i+=1
        print(self.instructions)
    def regvalue(self,register,val):
        if val<0:
            # print(val)
            self.reset()
            self.regval["FLAGS"][-4]='1'
            self.regval[register]=0
        elif val>=2e16:
            self.reset()
            self.regval["FLAGS"][-4]='1'
            self.regval[register]=2e16-1
        else:
            self.regval[register]=val
            self.reset()