from collections import defaultdict
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hashMap = defaultdict(int)
        paragraph = re.sub(r'[^a-zA-Z ]+', ' ', paragraph.lower())

        for word in paragraph.split():
            hashMap[word] += 1

        result = sorted([(k, v) for k, v in hashMap.items()], key=lambda x: -x[1])
        return next(k for k, v in result if k not in banned)
