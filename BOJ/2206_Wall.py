'''
import queue

N, M = map(int, input().split())
board = []
for _ in range(N):
    inp = list(input())
    d = list(map(int, inp))
    board.append(d)
cnt = [[0 for _ in range(M)] for _ in range(N)]
isVisited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def BFS():
    q = queue.Queue()
    q.put((0, 0, 0))
    isVisited[0][0] = [1, 1]
    while(not q.empty()):
        r, c, isBroken = q.get()
        if (r is N-1) and (c is M-1):
            cnt[r][c] += 1
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (nr < 0 or nr >= N or nc < 0 or nc >= M):
                if((isVisited[nr][nc][isBroken])):
                    continue
            if (board[nr][nc] == 0):
                cnt[nr][nc] = cnt[r][c] + 1
                isVisited[nr][nc][isBroken] = 1
                q.put((nr, nc, isBroken))
            elif (board[nr][nc] == 1) and (not isBroken):
                cnt[nr][nc] = cnt[r][c] + 1
                isVisited[nr][nc][1] = 1
                q.put((nr, nc, 1))


BFS()

if cnt[N-1][M-1] == 0:
    print(-1)
else:
    print(cnt[N-1][M-1])

for e in cnt:
    print(e)

# test = [1, 2, 3]
# test[1] = test[2] + 1
# print(test)
'''

from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
dist = [[[0, 0] for _ in range(m)] for _ in range(n)]
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)


def bfs():
    q = deque()
    q.append((0, 0, 0))
    dist[0][0][0] = 1
    while q:
        r, c, w = q.popleft()
        # while문 탈출조건 명시
        if r == n-1 and c == m-1:
            return dist[r][c][w]

        # 4방향으로 이동 시작
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            # 유효 범위를 벗어나거나 이미 방문했으면 가지 않는다.
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if dist[nr][nc][w]:  # 0이 아니라면 이미 방문한것
                continue

            # 게임판에서 0인 경우는 그냥 갈 수 있다.
            if a[nr][nc] == '0':
                dist[nr][nc][w] = dist[r][c][w] + 1
                q.append((nr, nc, w))

            # 게임판이 1이지만 벽부수기 기회가 남아있으면 그곳도 가본다.
            if a[nr][nc] == '1' and w == 0:
                dist[nr][nc][1] = dist[r][c][w] + 1
                q.append((nr, nc, 1))
    return -1


print(bfs())
for e in dist:
    print(e)
