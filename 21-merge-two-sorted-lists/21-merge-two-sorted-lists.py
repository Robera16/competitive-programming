# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1=list1
        head2=list2
        lt=[]
        while(head1 or head2):
            if head1==None:
                while(head2):
                    lt.append(head2.val)
                    head2=head2.next
                break
            elif head2==None:
                while(head1):
                    lt.append(head1.val)
                    head1=head1.next
                break
            elif head1.val <= head2.val:
                while(head1.val <= head2.val):
                    lt.append(head1.val)
                    head1=head1.next
                    if not head1:
                        break
                lt.append(head2.val)
                head2=head2.next
            else:
                while(head2.val <= head1.val):
                    lt.append(head2.val)
                    head2=head2.next
                    if not head2:
                        break
                lt.append(head1.val)
                head1=head1.next
        if not len(lt):
            head=None
            return head
        else:
            head=ListNode(lt.pop(0), None)
            itr=head
            for val in lt:
                node=ListNode(val, None)
                itr.next=node
                itr=node
               
            return head
       
                