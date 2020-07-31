'''
from itertools import combinations
from collections import deque
import copy

N, M, D = map(int, input().split())
board_ = []
cnt = 0
for i in range(N):
    temp = list(map(int, input().split()))
    cnt += temp.count(1)
    board_.append(temp)
board_.append([-1 for _ in range(M)])
archers = [i for i in range(M)]

dr = [0, -1, 0]
dc = [-1, 0, 1]


# def findEnemy(r_, c_, dist):
#     if board[r_][c_] == 1:
#         return (r_, c_, dist)
#     for i in range(3):
#         nr, nc = r_ + dr[i], c_ + dc[i]
#         if (nr < 0 or nr >= N or nc < 0 or nc >=M):
#             return

def calDist(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)


def findEnemy(c_, board):
    q = deque()
    q.append((N, c_))
    isVisit = [[0 for _ in range(M)] for _ in range(N+1)]
    isVisit[N][c_] = 1
    while (q):
        r, c = q.popleft()
        # 유효범위 바깥이면 제외

        # 새로 방문하는 지점을 큐에 삽입
        # board를 벗어나는지 여부와 방문여부는 항상 바로바로 체크
        for i in range(3):
            nr, nc = r+dr[i], c+dc[i]
            if (nr < 0 or nr > N or nc < 0 or nc >= M) or isVisit[nr][nc] == 1:
                continue
            q.append((nr, nc))
            isVisit[nr][nc] = 1

        if (calDist(r, c, N, c_) > D):
            continue
        if board[r][c] == 1:
            return (r, c)

    return (-1, -1)


ans = 0

for a in combinations(archers, 3):
    ret = 0
    cnt_ = cnt
    board = copy.deepcopy(board_)
    while (True):
        # 각 궁수의 타겟 좌표를 저장
        target = []
        for pos in a:
            target.append(findEnemy(pos, board))

        # 타겟이 없으면(-1, -1) 건너뛰고, 존재하면 ret의 크기를 한번만 키움
        for dt in target:
            r, c = dt
            if r == -1 and c == -1:
                continue
            ret += board[r][c]
            cnt_ -= board[r][c]
            board[r][c] = 0

        # 적 전진
        for i in range(M):
            if board[-2][i] == 1:
                cnt_ -= 1

        # 다 제거했으면 종료
        if cnt_ == 0:
            ans = max(ans, ret)
            break

        board = [[0 for _ in range(M)]] + board[:-2][:] + \
            [[-1 for _ in range(M)]]

    if cnt_ == 0:
        continue

print(ans)

# 블루의 풀이
# iknoom1107
#1002 041 254872
'''
from copy import deepcopy
from itertools import combinations

N, M, D = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]


def hunt(h, C):
    for d in range(1, D + 1):
        for dx in range(-d, d + 1):
            x, y = h + dx, N - (d - abs(dx))
            if 0 <= x < M and 0 <= y < N and C[y][x]:
                return x, y


def sol(H):
    C = deepcopy(B)  # 게임판을 그대로 복사
    ret = 0
    for _ in range(N):
        # E는 궁수마다 공격 가능한 좌표를 포함하는 집합니다.
        # 공격할수 없는 궁수는 hunt에서 None이 리턴되므로 None을 제거해줘야 한다.
        E = set(hunt(h, C) for h in H) - {None}

        # 궁수가 제거한 적의 수를 올려주고, 해당 좌표의 적도 제거한다.
        ret += len(E)
        for x, y in E:
            C[y][x] = 0

        # 적을 전진시킨다.
        for y in range(N - 1, 0, -1):
            C[y] = C[y - 1][:]
        C[0] = [0] * M

    return ret


# 이 부분은 combination을 만들어서 sol함수에 전달하는 부분이다.
# print(max(sol([i, j, k]) for i in range(M - 2)
#           for j in range(i + 1, M - 1) for k in range(j + 1, M)))

# 내가 바꿔본 부분
# 아래 구문의 괄호 위치에 주의하자.
print(max(sol(k) for k in combinations([i for i in range(M)], 3)))
