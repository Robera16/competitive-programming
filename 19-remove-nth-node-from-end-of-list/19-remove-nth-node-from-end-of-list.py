# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ln=1
        temp=head
        while temp.next:
            ln+=1
            temp=temp.next
        temp=head
        temp2=head.next
        if ln==1:
            head=None
            return head
        if ln==n:
            head=head.next
            return head
        ln=ln-n
        while(ln-1 and temp2):
            temp=temp2
            temp2=temp2.next
            ln-=1
        if temp2==None:
            temp.next=temp2
        else:
            temp.next=temp2.next
        return head
       
            