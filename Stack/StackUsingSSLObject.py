import SinglyLinkedList
class Stack:
    def __init__(self):
        self.obj=SinglyLinkedList.SLL()
    
    def is_empty(self):
        return self.obj.is_empty()



s=Stack()
print(s.is_empty())