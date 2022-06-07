# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums=[]
        while(head):
            nums.append(head.val)
            head=head.next
        
        k=i=0
        while(k < len(nums)//2):
            nums[i],nums[i+1]=nums[i+1],nums[i]
            i+=2
            k+=1
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
        
            