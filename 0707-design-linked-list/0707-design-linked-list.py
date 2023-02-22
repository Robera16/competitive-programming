class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
        
class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        else:
            temp = self.head
            while(index):
                temp = temp.next
                index-=1
            return temp.val      

    def addAtHead(self, val):
        node = Node(val, None)
        temp = self.head
        self.head = node
        node.next = temp 
        self.size+=1

    def addAtTail(self, val): 
        node = Node(val, None)
        temp=self.head
        if temp==None:
            self.head=node
        else:
            while(temp.next):
                temp=temp.next
            temp.next=node
        self.size+=1
        
    def addAtIndex(self, index, val):
        node = Node(val, None)
        temp=self.head
        if index > self.size:
            return 
        elif index==0:
            self.head=node
            node.next=temp   
        elif index:
            while(index-1):  
                temp=temp.next
                index-=1
            temp2=temp.next
            temp.next=node
            node.next=temp2
        self.size+=1
        
    def deleteAtIndex(self, index):
        temp=self.head
        if index < 0 or index >= self.size:
            return
        elif index==0:
            self.head=self.head.next
        elif index:
            while(index-1):
                temp=temp.next   
                index-=1
     
            temp.next=temp.next.next  
        self.size-=1