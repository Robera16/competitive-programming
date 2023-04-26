class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
       
        output=[[]]

        for i in range(len(nums)):
            for ele in combinations(nums, i+1):
                output.append(list(ele))

        return output