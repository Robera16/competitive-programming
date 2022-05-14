class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        unique_nums = list(set(nums))
        frequency=[]
        output=[]
        for num in unique_nums:
            frequency.append(nums.count(num))
      
        for i in range(k):
            index=frequency.index(max(frequency))
            output.append(unique_nums[index])
            frequency[index]=-1
        return output