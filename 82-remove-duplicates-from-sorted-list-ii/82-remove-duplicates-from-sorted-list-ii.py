# Definition for singly-linked list.
# class ListNode(object):
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        temp=head
        nums=[]
        while(temp):
            nums.append(temp.val)
            temp=temp.next
            
        uniques=list(set(nums))
        freq=[]
        for val in uniques:
            freq.append(nums.count(val))
        answer=[]
        i=0
        for val in freq:
            if val==1:
                answer.append(uniques[i])
            i+=1
        if not len(answer):
            return None
        answer.sort()
        temp=head
        for vall in answer:
            temp.val=vall
            prev=temp
            temp=temp.next
        prev.next=None
        return head
        
        
