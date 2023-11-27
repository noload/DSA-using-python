class PriorityQueue:
    def __init__(self):
        self.listObj=[]

    def is_empty(self):
        return len(self.listObj) == 0
            
    def push(self,data,priority):
        index=0
        while index<len(self.listObj) and self.listObj[index][1]<=priority:
            index+=1
        self.listObj.insert(index,(data,priority))

    def pop(self):
        if not self.is_empty():
            return self.listObj.pop(0)[0]
        else:
            raise IndexError("empty queue")

    def size(self):
        return len(self.listObj)
    
p=PriorityQueue()
p.push(20,1)
p.push(10,4)
p.push(30,2)
p.push(50,3)
p.push(80,6)
p.push(90,4)

while not p.is_empty():
    data=p.pop()
    print(data,end=" ")
