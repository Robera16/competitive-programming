# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        temp=head
        lt=[]
        tl=[]
        while(temp):
            lt.append(temp.val)
            temp=temp.next
        
        while(len(lt)):
            tl.append(lt.pop(0))
            if (len(lt)):
                tl.append(lt.pop())
        
        temp=head
        for vall in tl:
            temp.val=vall
            temp=temp.next
        
        
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        