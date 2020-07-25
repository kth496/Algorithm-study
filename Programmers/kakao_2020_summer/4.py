''' 풀이에 사용하는 전역변수
@ board : 문제에서 주어진 board를 저장함
@ n     : n*n 구조인 board의 n값을 의미함
@ dr, dc: row와 column을 이동할 때 사용함(흔히 dy dx로 표현하는 그것)
@ inf   : 무한대값을 의미함
@ dp    : dp[r][c][t]는 0행 0열에서 r행 c열까지 건설하는 도로 비용의 최소값을 나타냄
        : t는 코너를 돌아서 왔는지 아닌지를 나타냄(코너였으면 1)
'''
from collections import deque
board = []
n = 0
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
inf = float('inf')
dp = []


def solution(_input):
    # init
    global board
    global n
    global dp
    board = _input
    n = len(board)
    dp = [[[-1 for i in range(2)] for i in range(n)] for i in range(n)]
    r1, r2 = inf, inf

    board[0][0] = 1

    '''
    0행 0열에서 오른쪽이나 아래쪽으로만 출발할 수 있다.
    그래서 0행 1열 혹은 1행 0열이 벽으로 막히지 않은 경우에는 그곳에서 출발함.
    각각 방향으로 출발해서 답을 구한뒤 마지막에 최소값을 구해서 리턴한다.
    '''
    if (board[0][1] != 1):
        board[0][1] = 1
        r1 = solve2(0, 1, 0, 0, 100, 0)

    if (board[1][0] != 1):
        board[1][0] = 1
        r2 = solve2(1, 0, 0, 0, 100, 0)

    ans = [r1, r2]
    return min(ans)


def isValid(r, c):
    '''
    @ r : row
    @ c : column

    (r, c)가 board를 벗어나면 false 리턴
    이미 방문했거나 벽인 경우도 false를 리턴
    '''
    if ((r < 0) or (r == n) or (c < 0) or (c == n)):
        return False
    if (board[r][c] == 1):
        return False
    return True


def isCorner(prev_r, prev_c, next_r, next_c):
    '''
    현재 위치를 기준으로 이전위치(prev_) 와 다음위치(next_)를 비교하면,
    직각으로 꺾어서 진행했는지, 아니면 직선으로 진행했는지 알 수 있다.
    아래 계산식을 바탕으로 코너를 돌아서 갔으면 true를 리턴한다.
    '''
    dr_ = abs(prev_r - next_r)
    dc_ = abs(prev_c - next_c)
    return (dr_ and dc_)


def solve2(r, c, pr, pc, cost, t):
    '''
    @ r, c   : 현 위치 (r, c)를 나타낸다.
    @ pr, pc : 현 위치에 오기 전에 있었던 위치 (pr, pc)를 나타낸다.
    @ cost   : 현 위치에 오기까지 누적된 비용을 나타낸다.
    @ corner : 코너를 돌아서 왔는지를 나타낸다.
    '''

    ''' 
    dp[r][c]가 -1이라면 한번도 오지 않은 곳이니, cost값으로 표시한다. 
    이미 왔던 적이 있으면, 현재 cost값과 dp[r][c]를 비교한다. 
    cost가 dp[r][c]보다 작거나 같으면 cost로 갱신하고 계속 진행한다.
    만약 cost가 더 크다면, 이 루트는 살펴볼 가치가 없기 때문에 무한대를 리턴하고 종료
    '''
    if (dp[r][c][t] == -1):
        dp[r][c][t] = cost
    else:
        if (dp[r][c][t] >= cost):
            dp[r][c][t] = cost
        else:
            return inf

    ''' 도착지점에 도달하면 현재까지 누적된 cost를 그대로 반환 '''
    if (r == (n-1) and c == (n-1)):
        return cost

    ret = inf
    for i in range(4):
        '''
        @ nr  : next r의 의미로 다음으로 갈 row를 의미
        @ nc  : 위와 동일한 의미
        '''
        nr = r + dr[i]
        nc = c + dc[i]
        if (isValid(nr, nc)):
            board[nr][nc] = 1
            if (isCorner(pr, pc, nr, nc)):
                ''' 코너를 한번 돌면, 직선주로와 코너가 함께 생기므로 600원을 더함 '''
                cand = solve2(nr, nc, r, c, cost + 600, 1)
            else:
                cand = solve2(nr, nc, r, c, cost + 100, 0)
            ret = min(ret, cand)
            board[nr][nc] = 0
    return ret


# Test Case
t1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # ans : 900

# ans : 3800
t2 = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [
    0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]

# ans : 2100
t3 = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]

# ans : 3200
t4 = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0],
      [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]

# ans : 5300
t5 = [[0 for i in range(25)] for i in range(25)]

# ans : 3600
t6 = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [
    0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]

# ans : 6300
t7 = [[0, 1, 0, 0, 0, 1],
      [0, 1, 0, 1, 0, 0],
      [0, 1, 0, 1, 1, 0],
      [0, 0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 1],
      [1, 1, 1, 0, 0, 0]]

# ans : 1900
t8 = [[0, 0, 1],
      [1, 0, 0],
      [0, 1, 0], ]

# ans : 3000
t9 = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0]
]

print(solution(t9))


''' 다른사람의 풀이 

BFS로 푸는 방법이 훨씬 빠르고 명료하다.
'''


def calc_cost(cur_dir, nex_dir, cost):
    if (cur_dir == 'R' or cur_dir == 'L') and (nex_dir == 'L' or nex_dir == 'R'):
        return cost + 100
    if (cur_dir == 'D' or cur_dir == 'U') and (nex_dir == 'D' or nex_dir == 'U'):
        return cost + 100
    if (cur_dir == 'R' or cur_dir == 'L') and (nex_dir == 'D' or nex_dir == 'U'):
        return cost + 600
    if (cur_dir == 'D' or cur_dir == 'U') and (nex_dir == 'R' or nex_dir == 'L'):
        return cost + 600


def bfs(x, y, cost, direct):
    queue = deque([(x, y, cost, direct)])
    check = [[0 for _ in range(N)] for _ in range(N)]
    check[x][y] = 1
    while queue:
        x, y, cost, cur_dir = queue.popleft()
        if x == N-1 and y == N-1:
            answer.append(cost)
            continue
        for i, j, d in (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U'):
            new_x, new_y, new_cost = x+i, y+j, calc_cost(cur_dir, d, cost)
            if new_x < 0 or new_y < 0 or new_x >= N or new_y >= N:
                continue
            if not new_board[new_x][new_y]:
                if not check[new_x][new_y] or check[new_x][new_y] > new_cost:
                    check[new_x][new_y] = new_cost
                    queue.append((new_x, new_y, new_cost, d))


def solution(board):
    global N, check, new_board, answer
    answer = []
    N = len(board)
    new_board = [board[i][:] for i in range(N)]
    bfs(0, 0, 0, 'R')
    bfs(0, 0, 0, 'D')
    return min(answer)
