# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # find the length of  the list
        current, length, output = head, -1, 0
        while current:
            length+=1
            current = current.next
        
        while head:
            output+= pow(2,length)*head.val
            head = head.next
            length-=1
            
        return output