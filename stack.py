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

s=stack()
print(s.isEmpty())
s.push(10)
s.push(20)
s.push(30)
print(s.top())
print(s.isEmpty())
while not s.isEmpty():
    print(s.pop())
print(s.isEmpty())


