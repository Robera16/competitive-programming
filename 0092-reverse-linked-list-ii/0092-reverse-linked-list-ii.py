# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        leftNode, rightNode = None, None
        # traverse and find left and right node
        temp = head
        val = 1
        while temp:
            if val==left:
                leftNode = temp
            if val==right:
                rightNode = temp
            val+=1
            temp = temp.next
        
        prv = rightNode.next
        val = (right - left) + 1
        while val:
            temp = leftNode.next
            leftNode.next = prv
            prv = leftNode
            leftNode = temp
            val-=1
       
        leftt = head
        tempLeft = left
        while left-2 > 0:
            leftt = leftt.next
            left-=1
            
        
        if tempLeft > 1:
            leftt.next = rightNode
            return head
        else:
            return  rightNode