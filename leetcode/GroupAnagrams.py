from itertools import permutations
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_strs = defaultdict(list)
        for element in strs:
            key = ''.join(sorted(element))
            grouped_strs[key].append(element)
        return list(grouped_strs.values())

