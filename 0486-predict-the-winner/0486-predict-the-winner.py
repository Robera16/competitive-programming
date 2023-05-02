from functools import cache
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def player1_points(start: int, end: int):
            """
            Note that: player2 points would be -player_one_points(start, end)
            :param start: 
            :param end: 
            :return: 
            """
            if start > end:
                return 0
            elif end - start == 1:
                a, b = nums[start], nums[end]
                return abs(a - b)

            s, e = nums[start], nums[end]
            l, r = player1_points(start + 1, end), player1_points(start, end - 1)
            
            # as player1 has to pick either "s" or "e" so l and r calculated 
            # above will represent player2 points. So to get player1 points we 
            # need to change sign of numbers
            l, r = -l, -r

            return max(l + s, e + r)

        return player1_points(0, len(nums) - 1) >= 0