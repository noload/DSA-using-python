class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next=next
    
class LinkedList:
    def __init__(self,start=None):
        self.start = start
    

    def is_empty(self):
        return self.start == None

    def insert_at_begining(self,data):
        n=Node(data,self.start)
        if(not self.is_empty()):
            n.next = self.start
            self.start = n
        self.start = n
        
    def insert_at_end(self,data):
        n=Node(data,None)
        if(self.is_empty):
            self.start=n
        else:
            curr=self.start
            while(curr.next is not None):
                curr=curr.next
            curr.next = n
            n.next=None
    def display(self):
        curr=self.start
        while(curr.next is not None):
            print("########")
            print(curr.item,end=" ")
            curr=curr.next


list=LinkedList()


