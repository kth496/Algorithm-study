from collections import deque
F, S, G, U, D = map(int, input().split())

isVisited = [0 for _ in range(1, F+2)]


def dfs(x):
    ret = 0
    if x == G:  # 도착
        return 1

    for next_ in (x + U, x - D):
        if next_ > F:
            next_ = F
        if next_ < 1:
            next_ = 1
        if isVisited[next_] == 0:
            isVisited[next_] = 1
            ret += dfs(next_)
            isVisited[next_] = 0
    return ret


def bfs(x):
    q = deque()
    isVisited = [0 for _ in range(1, F+2)]

    # start
    q.append((x, 0))
    isVisited[x] = 1

    while (q):
        cur, dist = q.popleft()
        if cur == G:
            return dist
        for next_ in (cur + U, cur - D):
            #
            if next_ > F:
                continue
            if next_ < 1:
                continue

            #
            if isVisited[next_] == 0:
                isVisited[next_] = 1
                q.append((next_, dist+1))
    return -1


# print(dfs(S))
ans = bfs(S)
if ans == -1:
    print("use the stairs")
else:
    print(ans)
