class Solution:
    def isPalindrome(self, s: str) -> bool:
        pre = []
        for c in s:
            if c.isalnum():
                pre.append(c.lower())
        rev = pre[:]
        rev.reverse()

        if ''.join(pre) == ''.join(rev): return True
        else: return False
