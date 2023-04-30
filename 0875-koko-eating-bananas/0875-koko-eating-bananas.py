class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Edge case: 1 pile per hour
        if h == len(piles): 
            return max(piles)        

        def can_finish(speed):
            hour = 0
            for pile in piles:
                hour += 1 if pile < speed else math.ceil(pile/speed)
                if hour > h: 
                    return False
            return True

        # Binary Search
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right)//2

            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left