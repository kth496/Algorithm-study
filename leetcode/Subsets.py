from itertools import combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        for i in range(len(nums) + 1):
            ret += list(combinations(nums, i))
        return ret

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for num in nums:
            appended_ret = []
            for subset in ret:
                temp = subset[:]
                temp.append(num)
                appended_ret.append(temp)
            ret += appended_ret
        return ret
