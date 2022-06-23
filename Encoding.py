def encoding():
    opcode={"add":"10000","sub":"10001","ld":"10100","st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","xor":"11010","or":"11011","and":"11100","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010","movim":"10010","movr":"10011"}
#     # for i in instructions:
#         # instruction=i[0]
#         if instruction not in opcode:
#             if(instruction=="add"):
#                 opcode[instruction]="10000"
#             elif instruction=="sub":
#                 opcode[instruction]="10001"
#             elif instruction=="mov":
#                 if i[2][0][0]=="$":
#                     opcode[instruction]="10010"
#                 else:
#                     opcode[instruction]="10011"
#             elif instruction=="ld":
#                 opcode[instruction]="10100"
#             elif instruction=="st":
#                 opcode[instruction]="10101"
#             elif instruction=="mul":
#                 opcode[instruction]="10110"
#             elif instruction=="div":
#                 opcode[instruction]="10111"
#             elif instruction=="rs":
#                 opcode[instruction]="11000"
#             elif instruction=="ls":
#                 opcode[instruction]="11001"
#             elif instruction=="xor":
#                 opcode[instruction]="11010"
#             elif instruction=="or":
#                 opcode[instruction]="11011"
#             elif instruction=="and":
#                 opcode[instruction]="11100"
#             elif instruction=="not":
#                 opcode[instruction]="11101"
#             elif instruction=="cmp":
#                 opcode[instruction]="11110"
#             elif instruction=="jmp":
#                 opcode[instruction]="11111"
#             elif instruction=="jlt":
#                 opcode[instruction]="01100"
#             elif instruction=="jgt":
#                 opcode[instruction]="01101"
#             elif instruction=="je":
#                 opcode[instruction]="01111"
#             elif instruction=="hlt":
#                 opcode[instruction]="01010"
#     for i in opcode.keys():
#         print(i,opcode[i])
# encoding()

            
              


