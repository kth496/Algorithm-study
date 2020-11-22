from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ret = 0
        lo = 0
        hi = len(height) - 1
        while lo < hi:
            cur_water = (hi - lo) * min(height[lo], height[hi])
            ret = max(ret, cur_water)
            if height[hi] > height[lo]:
                lo += 1
            else:
                hi -= 1
        return ret
