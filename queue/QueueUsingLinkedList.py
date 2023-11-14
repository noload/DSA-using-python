from Node import Node
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    
    def is_empty(self):
        return self.front==None
    
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next_node=n
        self.rear=n
        self.item_count+=1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("empty queue")
        elif self.front == self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next_node
        self.item_count-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Index Error")
        else:
            return self.front.get_value()
    def get_rear(self):
        if self.is_empty():
            raise IndexError("index error")
        else:
            return self.rear.get_value()
    
    def size(self):
        return self.item_count
    
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.get_front())
print(q1.get_rear())
q1.dequeue()

print(q1.get_front())
print(q1.get_rear())