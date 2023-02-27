# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        if not temp:
            return head
        nxt=head.next
        while(nxt):
            while(nxt and (temp.val==nxt.val)):
                nxt=nxt.next
            temp.next=nxt
            temp=nxt
            if not nxt:
                break
            else:
                nxt=nxt.next
        return head