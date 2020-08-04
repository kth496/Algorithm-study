import sys
sys.setrecursionlimit(9999)

c = 0
r = 0
cnt = 0
dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, 0, 1, -1, 0, 1, -1]
board = []
isVisited = []


def dfs(y, x):
    if y < 0 or x < 0 or y >= r or x >= c or isVisited[y][x] == 1 or board[y][x] == 0:
        return
    isVisited[y][x] = 1
    for i in range(8):
        dfs(y + dr[i], x + dc[i])


ans = []
while (True):
    c, r = map(int, input().split())
    cnt = 0
    if (c == 0):
        # print(ans)
        exit()
    board = [list(map(int, input().split())) for _ in range(r)]
    isVisited = [[0 for _ in range(c)] for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if board[y][x] == 1 and isVisited[y][x] == 0:
                cnt += 1
                dfs(y, x)
    print(cnt)
    # ans.append(cnt)
