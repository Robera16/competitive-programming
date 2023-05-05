class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return int(round((sum(set(nums)) - sum(nums)/3)*1.5))
        # explantion
        #[x,x,x,y,z,z,z] => [3x,3z,y]
        # uniques [x, z, y]
        # x+z+y - (3x+3z+y)/3
        # y -y/3 => 2y/3
        # multiply the number by 2/3(1.5) to find y
        # to assume the value of any fracton of numbers left during division use rounding