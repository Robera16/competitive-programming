class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
       
        while(k):
            nums[:0] = [nums.pop()]
            k-=1
        