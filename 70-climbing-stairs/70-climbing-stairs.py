class Solution:
    def climbStairs(self, n: int) -> int:
        arr=[1,1]
        if n <2:
            return arr[n]
        for i in range(2,n+1):
            arr.append(arr[i-1]+arr[i-2])
        return arr[n]