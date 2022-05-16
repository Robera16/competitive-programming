# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        counter=0
        while temp is not None:
            counter+=1
            temp = temp.next
        counter//=2
        for i in range(counter):
            head = head.next         
        return head
        
        
        
        