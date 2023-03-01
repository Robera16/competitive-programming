# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(None, None)
        output.next = ListNode(head.val, None)
        head = head.next

        while head:  
            current=output
            while current.next and current.next.val < head.val:
                current = current.next
            nxt = current.next
            current.next = ListNode(head.val, nxt)
            head = head.next
            
        return output.next