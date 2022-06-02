# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=num2=''
        while(l1):
            num1+=str(l1.val)
            l1=l1.next
        num1=num1[::-1]
        while(l2):
            num2+=str(l2.val)
            l2=l2.next
        num2=num2[::-1]
        head=itr=None
        for c in str(int(num1)+int(num2))[::-1]:
            if not head:
                head=ListNode(c, None)
                itr=head
            else:
                node=ListNode(c, None)
                itr.next=node
                itr=node
        return head
                
   
            
        