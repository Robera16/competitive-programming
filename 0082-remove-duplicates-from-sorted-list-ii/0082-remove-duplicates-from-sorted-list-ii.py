# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        repeated = {}
        
        while(current):
            if current.val not in repeated:
                repeated[current.val] = False
            else:
                repeated[current.val] = True
            current = current.next
        
        prev = None
        current = head
        while(current):
            if (repeated[current.val]):
                while (repeated[current.val]):
                    current = current.next
                    if current==None:
                        if not prev:
                            return None
                        else:
                            prev.next = None
                            return head
                if not prev:
                    head = current
                    prev = current
                else:
                    prev.next = current
                    prev = current
            else:
                prev= current   
            current = current.next
           
        return head

