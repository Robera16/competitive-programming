# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
      
        temp = head
        lower, greater, first_greater, first_lower = None, None, None, None
        while(temp):
            if temp.val < x:
                if not lower:
                    lower = temp
                    first_lower = lower
                else:
                    lower.next = temp
                    lower = temp
            else:
                if not greater:
                    greater = temp
                    first_greater = greater
                else:
                    greater.next = temp
                    greater = temp
            temp = temp.next
            
        if lower:
            lower.next = first_greater
        if greater:
            greater.next = None
        if first_lower:
            return first_lower
        else:
            return first_greater
        