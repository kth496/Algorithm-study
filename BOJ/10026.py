from collections import deque

N = int(input())
board = [list(input()) for _ in range(N)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def bfs(r_, c_):
    q = deque()
    q.append((r_, c_))
    col = board[r_][c_]
    isVisited[r_][c_] = 1
    while (q):
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (nr < 0 or nr >= N or nc < 0 or nc >= N):
                continue
            elif (isVisited[nr][nc] == 1 or board[nr][nc] != col):
                continue
            else:
                isVisited[nr][nc] = 1
                q.append((nr, nc))
    return 1


'''
BFS 로 특정 범위의 덩어리를 인지하는 방법은?
-> 그냥 BFS돌리고 리턴시키면 그게 하나의 덩어리 끝임
'''
isVisited = [[0 for _ in range(N)] for _ in range(N)]
ret = 0
for y in range(N):
    for x in range(N):
        if isVisited[y][x] == 0:
            ret += bfs(y, x)

for y in range(N):
    for x in range(N):
        if board[y][x] == 'G':
            board[y][x] = 'R'

isVisited = [[0 for _ in range(N)] for _ in range(N)]
ret2 = 0
for y in range(N):
    for x in range(N):
        if isVisited[y][x] == 0:
            ret2 += bfs(y, x)


print(ret, ret2)
