# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p = headA
        q = headB
       
        while p and q:
            if p == q:
                return p
            else:
                if p.next==None and q.next==None:
                    return None
                if p.next==None:
                    p = headB
                else:
                    p = p.next
                if q.next==None:
                    q = headA
                else:
                    q = q.next
                
        
        
        