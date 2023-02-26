# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        if not head:
            return 
                      # odd = 3, even = none
        odd = head    # 1->2>3  1->3->2->none
        even = odd.next
        temp = even # to connect the last odd with the first even
        while even:
            # even = odd.next
            if even.next:
                odd.next = even.next
                odd = even.next
                even.next = odd.next
                even = odd.next
                if not odd.next:
                    odd.next=temp
            else:
                odd.next=temp
                even=None
        return head