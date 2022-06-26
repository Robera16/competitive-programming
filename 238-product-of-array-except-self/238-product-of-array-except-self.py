class Solution(object):
    def productExceptSelf(self, nums):
        left=[]
        right=[]
        left.append(nums[0])
        for i in range(1, len(nums)):
            left.append(left[-1]*nums[i])
        
        right.append(nums.pop())
        while(len(nums)):
            right.append(right[-1]*nums.pop())
        right.reverse()
        answer=[]
        for j in range(len(left)):
            if j==0:
                answer.append(right[j+1])
            elif j==len(left)-1:
                answer.append(left[j-1])
            else:
                answer.append(left[j-1]*right[j+1])
      
        return answer
        