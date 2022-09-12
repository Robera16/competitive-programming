class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class SLinkedList:
    def __init__(self):
        self.head = None
        
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        list1 = SLinkedList()
        list1.head = None
         
        for val in range(n):
            if not list1.head:
                list1.head=Node(val+1, None)
                prv=list1.head
            else:
                node=Node(val+1, None)
                prv.next=node
                prv=node
        # circular
        prv.next = list1.head
        
        prev = list1.head
        previous_node = prev
        if prev.next.val == previous_node.val:
            return  previous_node.val
        kk=k
        k-=1
        if k==0:
            return prv.val
        else:
            while(prev.next):
                prev = prev.next
                k-=1
                if k == 0:
                    if prev.next.val == previous_node.val:
                        return previous_node.val
                    previous_node.next = prev.next
                    previous_node = prev.next
                    prev = prev.next
                    k=kk-1
                else:
                    previous_node = previous_node.next
        