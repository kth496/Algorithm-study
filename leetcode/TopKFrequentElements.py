from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_count = defaultdict(int)
        for num in nums:
            number_count[num] += 1
        sorted_dict = sorted(number_count.items(), key=lambda x: x[1], reverse=True)
        return list(map(lambda x: x[0], sorted_dict))[:k]

