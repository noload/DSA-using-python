from SinglyLinkedList import SLL
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
class CycleList:
    def __init__(self,head=None):
        self.head = head

    def hasCycle(self,head):
        slow=head
        fast = head
        while (fast.next.next != None):
            if slow is fast:
                return True
            slow=slow.next
            fast=fast.next.next

