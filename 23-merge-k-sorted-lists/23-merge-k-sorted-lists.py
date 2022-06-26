# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        nums=[]
        for val in lists:
            temp=val
            while(temp):
                nums.append(temp.val)
                temp=temp.next
        
        nums.sort()
        head=None
        for val in nums:
            node=ListNode(val, None)
            if not head:
                head=node
                prev=head
            else:
                prev.next=node
                prev=node
        return head
        