class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k==0:
            new_list=set(nums)
            count=0
            for val in new_list:
                if nums.count(val) > 1:
                    count+=1
            return count
        else:
            my_dict = dict() 
            for index,value in enumerate(nums):
                my_dict[value] = index
            count=0
            for val in set(nums):
                if val+k in my_dict.keys():
                    count+=1
            return count