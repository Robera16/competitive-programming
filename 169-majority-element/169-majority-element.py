class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct={}
        for val in nums:
            if str(val) in dct:
                dct[str(val)]=dct[str(val)]+1
            else:
                dct[str(val)]=1  
        dct = {k: v for k, v in sorted(dct.items(), key=lambda v: v[1], reverse=True)}
        return next(iter(dct))
        
        