from collections import deque

N, K = map(int, input().split())
MAXN = 100000


def bfs(n, k):
    ret = 0
    q = deque([n])
    visited = [-1] * (MAXN+1)
    visited[n] = 0
    while (q):
        cur = q.popleft()
        if cur == k:
            return visited[K]
        for nextn in (cur+1, cur-1, cur*2):
            if nextn >= 0 and nextn <= MAXN and visited[nextn] == -1:
                visited[nextn] = visited[cur] + 1
                q.append(nextn)


print(bfs(N, K))
