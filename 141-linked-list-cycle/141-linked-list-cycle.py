# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tracker=100001
        temp=head
        if not temp:
            return False
        temp.val=tracker
        while(temp.next):
            temp=temp.next
            if temp.val==tracker:
                return True
            else:
                temp.val=tracker
        return False