from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
# print(board)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs(r_, c_):
    ''' BFS의 정형화된 구조
    @ q     :   BFS를 위해 사용하는 큐
    @ v     :   방문 여부를 저장하는 visited를 의미한다.
                추가로, BFS에서 최단거리를 나타내야하는 문제에서는 
                v배열의 값이 (r_, c_)로부터의 최단거리를 의미한다.
    @ ret:  :   문제에따라 ret이 필요한 경우와 그렇지 않은 경우가 나뉜다.

    출발 지점은 무조건 표시를 해둬야한다. 그렇지 않으면 초반 단계에서 출발 지점을 재방문한다.

    while 문은 q가 비어있지 않은 경우 계속 순회하도록 한다.

    문제의 요구대로 for문을 통해 방문한다. 일반적으로 4방면으로 진행하며, 
    방향은 전역배열 dr, dc로 관리하면 편하다.
    for 문 내부에서는 "방문 불가능한 조건" 을 or 문으로 전부 엮은 뒤, continue를 시키는 쪽이 간결하다.
    방문 가능한 경우에는 q에 방문 가능한 좌표를 삽입하고, 방문 여부 v를 곧바로 체크해주어야 한다.
    그렇지 않으면 중복으로 방문해서 비효율적이기 때문이다.
    문제의 조건에 따라 v[nr][nc] = v[r][c] + 1 과 같은 구문으로 처리하면 최단거리도 한번에 알 수 있다.
    '''
    q = deque()
    q.append((r_, c_))
    v = [[0 for _ in range(M)] for _ in range(N)]
    v[r_][c_] = 1  # 출발지점을 표시해두지 않으면 한번 이동후 출발지점으로 다시 돌아오는 문제 발생
    ret = 0
    while (q):
        r, c = q.popleft()

        isCorner = True
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if (nr < 0 or nr >= N or nc < 0 or nc >= M or v[nr][nc] != 0 or board[nr][nc] == 'W'):
                continue  # 이동 불가한 경우 처리
            else:
                isCorner = False
                q.append((nr, nc))
                v[nr][nc] = v[r][c] + 1

        if isCorner:  # 구석에 도착하면 이동 거리를 저장
            ret = max(ret, v[r][c])
    return ret - 1  # 위에서 출발지점을 1로 설정했기 때문에 최종 이동거리는 1을 빼야한다.


chk = [[0 for _ in range(M)] for _ in range(N)]
ans = 0
for y in range(N):
    for x in range(M):
        if board[y][x] == 'L' and chk[y][x] == 0:
            chk[y][x] = 1
            ans = max(ans, bfs(y, x))
print(ans)


'''
문제 접근 방법

육지내에서 서로 가장 먼 구석 지점을 찾아야한다. 육지를 다 돌아보지 않고서는 이 거리를 알 수 없다.
따라서 육지의 각 지점마다 전부 BFS를 수행한다. 이때 BFS로 탐색한 결과는 특정 지점에서 가장 먼 육지지점까지의 거리를 리턴한다.
리턴된 값을 max로 묶어나가면 결국 육지의 모든 지점에서 BFS를 계산해본 결과값의 최대값을 얻을 수 있다. 그것이 답이다.



'''
