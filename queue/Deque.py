class Deque:
    def __init__(self):
       self.listObj=[]

    
    def is_empty(self):
        return len(self.listObj) == None
    
    
    def insert_front(self,data):
        self.listObj.insert(0,data)
    
    def insert_rear(self,data):
        self.listObj.append(data)
    
    def delete_front(self):
        if not self.is_empty():
            value_to_remove=self.listObj[0]
            self.listObj.pop(0)
            return value_to_remove
        else:
            raise IndexError("queue empty")
    
    def delete_rear(self):
        if not self.is_empty():
            value_to_remove=self.listObj[len(self.listObj)-1]
            self.listObj.pop()
            return value_to_remove
        else:
            raise IndexError("queue empty")
        
    




q=Deque()
q.insert_front(10)
q.insert_front(10)
print(q.delete_rear())
q.insert_rear(30)
q.delete_rear(40)