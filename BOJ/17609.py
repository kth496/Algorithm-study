T = int(input())


def isPal(s, turn):
    n = len(s)
    key = (n - 1)//2
    isPos = 0
    for i in range(key+1):
        if (s[i] != s[n-1-i]):
            if turn:
                return 2
            ret1 = isPal(s[:i] + s[i+1:], True)
            ret2 = isPal(s[:n-1-i] + s[n-i:], True)
            isPos = min(ret1, ret2) + 1
            break
    return isPos-1 if isPos == 3 else isPos


for _ in range(T):
    d = input()
    print(isPal(d, False))
