import sys
from collections import deque

input = sys.stdin.readline

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0: exit(0)

    dr = [0, 0, 1, -1, 0, 0]
    dc = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    v = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    board = []

    st = ()
    ed = ()
    for z in range(L):
        floor = []
        for r in range(R):
            row = list(input())[:-1]
            floor.append(row)
            for c, val in enumerate(row):
                if val == 'S':
                    st = (r, c, z)
                if val == 'E':
                    ed = (r, c, z)
        input()
        board.append(floor)

    q = deque()
    q.append((st, 0))
    r, c, z = st
    v[z][r][c] = True
    ans = 9999999
    
    while len(q) > 0:
        curPos, time = q.popleft()
        r, c, z = curPos
        if board[z][r][c] == "E":
            ans = min(ans, time)
            continue
        for i in range(6):
            nr, nc, nz = r + dr[i], c + dc[i], z + dz[i]
            if nr < 0 or R <= nr or nc < 0 or C <= nc or nz < 0 or L <= nz:
                continue
            if board[nz][nr][nc] != '#' and not v[nz][nr][nc]:
                v[nz][nr][nc] = True
                nxt_pos = (nr, nc, nz)
                q.append((nxt_pos, time + 1))
                
    if ans == 9999999: print("Trapped!")
    else: print("Escaped in %d minute(s)." % ans)
