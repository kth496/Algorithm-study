from collections import deque
import sys

input = sys.stdin.readline

chk = [0 for _ in range(10000)]

for i in range(2, 10000):
    if chk[i] == 1: continue
    for j in range(i * i, 10000, i):
        chk[j] = 1


def search(st, tar, v):
    ret = 9999
    q = deque()
    q.append((st, 0))
    v[st] = 1
    while len(q) > 0:
        cur, cnt = q.popleft()
        if cur == tar:
            ret = min(ret, cnt)
            continue
        for i in range(4):
            form = '%04d' % cur
            rad = int(form[i])
            for j in range(10):
                rad_n = (rad + j) % 10
                next_ = list(form)
                next_[i] = str(rad_n)
                next_ = ''.join(next_)
                next_ = int(next_)
                if chk[next_] == 0 and v[next_] == 0 and next_ > 1000:
                    v[next_] = 1
                    q.append((next_, cnt + 1))
    return ret


N = int(input())
for _ in range(N):
    st, ed = map(int, input().split())
    if st == ed:
        print(0)
        continue
    v = [0 for _ in range(10000)]
    ret = search(st, ed, v)
    if ret == 9999:
        print("Impossible")
    else:
        print(ret)
