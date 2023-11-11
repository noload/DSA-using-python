class Queue:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("queue is empty can't remove")
        
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("empty queue")
    
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("queue empty")
    
    def size(self):
        return len(self.items)
    
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print("size of queue",q1.size())
q1.dequeue()
print("size of queue",q1.size())
print("front= ",q1.get_front()," rear = ",q1.get_rear())