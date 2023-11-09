from SinglyLinkedList import *;
class Stack:
    def __init__(self):
        self.stackObj=SLL()
        self.count=0
    
    def is_empty(self):
        return self.stackObj.is_empty()
    
    def push(self,data):
        self.stackObj.insert_at_start(data)
        self.count+=1
    
    def pop(self):
        if not self.is_empty():
            self.stackObj.delete_first()
            self.count-=1
    
    def peek(self):
        if not self.is_empty():
            return self.stackObj.start.item
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return self.count;

stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top element is ",stack.peek())
stack.pop()
print("Top element is ",stack.peek())
