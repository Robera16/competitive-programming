# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        prev=node
        current=node.next
        temp=prev
        while(current):
            prev.val=current.val
            current=current.next
            temp=prev
            prev=prev.next
        temp.next=None
        