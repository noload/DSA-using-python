from SinglyLinkedList import *
class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.itemCount=0
    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.itemCount+=1
    
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.itemCount-=1
        else:
            raise IndexError("Stack is Empty")
    
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is Empty")
    
    def size(self):
        return self.itemCount

s=Stack()
s.push(20)
s.push(30)
s.push(40)
print("Top element ",s.peek())
s.pop()
print("Top element ",s.peek())
print("Items ",s.size())