class Node:
    def __init__(self,item,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next

class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.itemCount=0
    def is_empty(self):
        return self.front == None
    
    def inserFront(self,data):
        self.itemCount+=1
        n=Node(data,None,self.front)
        if self.is_empty():
            self.rear=n
        else:
            self.front.prev=n
        self.front=n
        

    def inserRear(self,data):
        n=Node(data,self.rear,None)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.itemCount+=1

    def deleteFront(self):
        if self.is_empty():
            raise IndexError("empty")
        if self.front == self.rear:
            self.front=None
            self.rear = None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.itemCount-=1

    def deleteRear(self):
        if self.is_empty():
            raise IndexError("empty")
        if self.front == self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.itemCount-=1
    
    def get_Front(self):
        if self.is_empty():
            raise IndexError("empty")
        return self.front.item
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Empty")
        return self.rear.item
    
    def get_size(self):
        return self.itemCount
    
d1=Deque()
print(d1.is_empty())
d1.inserFront(10)
d1.inserFront(20)
print(d1.get_size())