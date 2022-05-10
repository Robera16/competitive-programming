class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer=[True]*len(l)
        temp=[]
        for i in range(len(l)):
            temp=nums[l[i]:r[i]+1]
            temp.sort()
            for j in range(len(temp)-1):
                if temp[j+1]-temp[j]!=temp[1]-temp[0]:
                    answer[i]=False
                    break
        return answer