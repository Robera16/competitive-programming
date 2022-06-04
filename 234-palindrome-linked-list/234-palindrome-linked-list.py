# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums=[]
        while(head):
            nums.append(head.val)
            head=head.next
        k=0
        while(k < (len(nums)/2)):
            if nums[k]!=nums[len(nums)-(k+1)]:
                return False
            k+=1
        return True
            