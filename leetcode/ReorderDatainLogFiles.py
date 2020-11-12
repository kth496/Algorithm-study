class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        for log in logs:
            log_s = log.split()
            if log_s[1].isnumeric():
                digit.append(log)
            else:
                letter.append(log)

        def comp(x: str):
            x = x.split()
            return x[1:] + [x[0]]

        letter.sort(key=comp)
        return letter + digit
