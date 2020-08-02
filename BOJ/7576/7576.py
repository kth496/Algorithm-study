from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

q = deque()
dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]
isVisit = [[0 for _ in range(M)] for _ in range(N)]


for r, row in enumerate(board):
    for c, e in enumerate(row):
        if e == 1:
            q.append((r, c))
            isVisit[r][c] = 1


while (q):
    r, c = q.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if (nr < 0 or nr >= N or nc < 0 or nc >= M) or (isVisit[nr][nc] == 1) or board[nr][nc] == -1:
            continue
        board[nr][nc] = board[r][c] + 1
        isVisit[nr][nc] = 1
        q.append((nr, nc))

ans = 0

for row in board:
    for e in row:
        if e == 0:
            print(-1)
            exit()
        else:
            ans = max(ans, e)
print(ans-1)

# 고수의 풀이(cpp)
# WeissBlume
""" 
#include<cstdio>
#include<algorithm>
#include<queue>
#define x second
#define y first
using namespace std;
typedef pair<int,int> ii;

int N, M, lv, K,
	dx[] = {-1, 0, 1, 0},
	dy[] = {0, 1, 0, -1};

int main()
{
	char f[1001][1001] = {},
		 v[1001][1001] = {};
	scanf("%d%d", &M, &N);

	queue<ii> q;

	for (int i = 0; i < N; i++) {
		for (int j = 0, a; j < M; j++) {
			scanf("%d", &a);
			f[i][j] = a;
			K += !a;
			if (a == 1) {
				q.push(ii(i, j));
				v[i][j] = 1;
			}
		}
	}

	for (lv = 0; !q.empty() && K; ++lv) {
		for (int s = q.size(); s--;) {
			ii u = q.front(); q.pop();
			for (int k = 0; k < 4; k++) {
				int nx = u.x + dx[k],
					ny = u.y + dy[k];
				if (nx >= 0 && ny >= 0 &&
					nx < M && ny < N && !v[ny][nx] &&
					!f[ny][nx]) {
					q.push(ii(ny, nx));
					--K;
					v[ny][nx] = 1;
				}
			}
		}
	}

	printf("%d\n", K ? -1 : lv);

	return 0;
}

"""
