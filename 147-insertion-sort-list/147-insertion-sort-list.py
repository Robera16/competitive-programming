# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums=[]
        while(head):
            nums.append(head.val)
            head=head.next
        nums.sort()
        head=None
       
        for val in nums:
            if not head:
                head=ListNode(val, None)
                prv=head
            else:
                node=ListNode(val, None)
                prv.next=node
                prv=node
        return head
        