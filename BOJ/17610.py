# 3
# 1 5 7

from itertools import combinations

# K = int(input())
# W = list(map(int, input().split()))
# chk = [0 for _ in range(sum(W)+1)]


def make(s, ret):
    if len(s) == 0:
        chk[abs(ret)] = 1
        return
    next_ = s[0]
    make(s[1:], ret + next_)
    make(s[1:], ret - next_)


# for i in range(len(W)+1):
#     for c in combinations(W, i):
#         make(c, 0)

# chk = chk[1:]
# ans = 0
# for a in chk:
#     if a == 0:
#         ans += 1
# print(ans)

K = int(input())
W = list(map(int, input().split()))
chk = [0 for _ in range(sum(W)+1)]
toChk = int(input())
target = list(map(int, input().split()))

for i in range(len(W)+1):
    for c in combinations(W, i):
        make(c, 0)

for t in target:
    if (chk[t] == 1):
        print("Y ", end="")
    else:
        print("N ", end="")
