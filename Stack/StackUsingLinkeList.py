class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top=None
        self.item_count=0
    
    def is_empty(self):
        return self.top == None
    
    def push(self,data):
        n=Node(data)
        n.next=self.top
        self.top=n
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            data=self.top.item
            self.top=self.top.next
            self.item_count-=1
            return data
        else:
            raise IndexError("Stack Empty")

    def size(self):
        return self.item_count
    
    def peek(self):
        return self.top.item


s=Stack()
s.push(10)
s.push(20)
print(s.peek())
s.push(30)
s.push(40)
print(s.peek())

print(s.pop())
print(s.size())