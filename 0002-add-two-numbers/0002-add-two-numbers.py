# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        head, carry = temp, 0
        while l1 or l2:
            if l1 and l2:
                num = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                num = l1.val + carry
                l1 = l1.next
            elif l2:
                num = l2.val + carry
                l2 = l2.next
            
            temp.next = ListNode(num % 10, None)
            temp = temp.next
            carry = num // 10
                
        if carry:
            temp.next = ListNode(carry, None)
            
        return head.next