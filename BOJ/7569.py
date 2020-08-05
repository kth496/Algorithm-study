from collections import deque

M, N, H = map(int, input().split())

box = []
for _ in range(H):
    board = [list(map(int, input().split())) for k in range(N)]
    box.append(board)


q = deque()

for h, board in enumerate(box):
    for r, row in enumerate(board):
        for c, e in enumerate(row):
            if e == 1:
                q.append((h, r, c))

isVisited = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]

dr = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

while (q):
    h, r, c = q.popleft()
    for i in range(6):
        nh, nr, nc = h + dh[i], r + dr[i], c + dc[i]
        if nh < 0 or nr < 0 or nc < 0 or nh >= H or nr >= N or nc >= M or isVisited[nh][nr][nc] == 1 or box[nh][nr][nc] != 0:
            continue
        box[nh][nr][nc] = box[h][r][c] + 1
        isVisited[nh][nr][nc] = 1
        q.append((nh, nr, nc))

ans = 0
for floor in box:
    for row in floor:
        for e in row:
            if e == 0:
                print(-1)
                exit()
            else:
                ans = max(ans, e)
print(ans-1)
