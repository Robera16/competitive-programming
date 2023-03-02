# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
    
        pointer = head
        dct = {}
        while pointer:
            if pointer in dct:
                return pointer
            else:
                dct[pointer]=True
            pointer = pointer.next
        return None