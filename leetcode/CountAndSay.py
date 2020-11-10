class Solution:
    def countAndSay(self, n: int) -> str:
        ret = "1"

        def recur(m: int) -> str:
            nonlocal ret
            if m == n: return ret
            ret = ''.join(
                str(len(list(g))) + k
                for k, g in groupby(ret))
            return recur(m + 1)

        return recur(1)

    def countAndSay2(self, n: int) -> str:
        if n == 1: return "1"
        ret = self.countAndSay(n - 1)
        return ''.join(
            str(len(list(g))) + k
            for k, g in groupby(ret))
