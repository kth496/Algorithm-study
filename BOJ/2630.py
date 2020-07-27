from sys import stdin

input = stdin.readline

N = int(input())
board = [list(input().split()) for _ in range(N)]
ans = [0, 0]


def DC(r_, c_, N_):
    col = board[r_][c_]
    isPos = True
    ret = [0, 0]

    for r in range(r_, r_ + N_):
        for c in range(c_, c_ + N_):
            if board[r][c] != col:
                isPos = False
                break
        if not isPos:
            break
    if isPos:
        ret[int(col)] += 1
        return ret

    else:
        nextN = N_//2
        tmp = []
        tmp.append(DC(r_, c_, nextN))
        tmp.append(DC(r_ + nextN, c_, nextN))
        tmp.append(DC(r_, c_ + nextN, nextN))
        tmp.append(DC(r_ + nextN, c_ + nextN, nextN))
        for e in tmp:
            ret[0] += e[0]
            ret[1] += e[1]
        return ret


ans = DC(0, 0, N)
for a in ans:
    print(a)
