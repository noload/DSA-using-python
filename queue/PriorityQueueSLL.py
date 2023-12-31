class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next


class PriorityQueue:
    def __init__(self):
        self.start=None
        self.itemCount=0
    

    def  push(self,data,priority):
        n=Node(data,priority)
        if not self.start or priority < self.start.priority:
            n.next=  self.start
        else:
            temp=self.start
            while temp.next and temp.next.priority <= priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.itemCount+=1


    def is_empty(self):
        return self.itemCount ==0
    
    def pop(self):
        if not self.is_empty():
            removeData=self.start.item
            self.start=self.start.next
            self.itemCount-=1
            return removeData
        else:
            raise IndexError("empty")
    
    def size(self):
        return self.itemCount
    
p=PriorityQueue()
p.push(20,1)
p.push(10,4)
p.push(30,2)
p.push(50,3)
p.push(80,6)
p.push(90,4)

while not p.is_empty():
    print(p.pop())