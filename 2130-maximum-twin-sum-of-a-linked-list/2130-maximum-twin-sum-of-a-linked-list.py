# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums=[]
        output=0
        while(head):
            nums.append(head.val)
            head=head.next
        k=0
        while(k<(len(nums)/2)):
            output=max(output, (nums[k]+nums[(len(nums))-1-k]))
            k+=1
        return output