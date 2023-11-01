class Stack(list):
    def is_empty(self):
        return len(self)== None
    
    def push(self,data):
        return self.append(data)
    
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty")
    
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self)
    
    def insert(self,index,data):
        raise AttributeError("Not able to insert in Stack")

s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.peek())