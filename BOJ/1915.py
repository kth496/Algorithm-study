from collections import deque

N, M = map(int, input().split())

# board = [list(input()) for _ in range(N)]

board = [[0 for _ in range(M+3)] for _ in range(N+3)]

for i in range(1, N+1):
    tmp = list(input())
    for j in range(1, M+1):
        board[i][j] = int(tmp[j-1])

ans = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i][j] != 0:
            board[i][j] = min(board[i-1][j], board[i]
                              [j-1], board[i-1][j-1]) + 1
            ans = max(ans, board[i][j])
print(ans**2)

# for row in board:
#     print(row)

# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]

# diag = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# def isRect(r1, c1, r2, c2):
#     mnr, mxr = min(r1, r2), max(r1, r2)
#     mnc, mxc = min(c1, c2), max(c1, c2)

#     # r,c는 r1, c1과 r2, c2를 대각선 꼭지점으로 하는 정사각형 내부의 한 점이다.
#     for r in range(mnr, mxr+1):
#         for c in range(mnc, mxc+1):
#             if (r < 0 or r >= N or c < 0 or c >= M or board[r][c] == '0'):
#                 return False
#     return True

# def find(r_, c_):
#     ret = 0
#     for i in range(4):  # 4방향 대각선으로 탐색 시작
#         for j in range(1003):
#             # 대각선 방향으로 j배 만큼 이동한다.
#             # 만약 이 범위 안에서 정사각형이 만들어지면, 한 변의 길이가 j이다.
#             nr, nc = r_ + diag[i][0] * j, c_ + diag[i][1] * j
#             if isRect(r_, c_, nr, nc):
#                 ret = max(ret, j)
#             else:
#                 break
#     return ret + 1

# ans = 0
# for y in range(N):
#     for x in range(M):
#         if board[y][x] == '1':
#             ans = max(ans, find(y, x))
# print(ans ** 2)

'''
#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>
#include <utility>

using namespace std;

int n, m;
char map[1001][1001];
int d[1001][1001];

int res;

int main(void)
{
    // freopen("input.txt", "r", stdin);

    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) {
        scanf("%s", map[i]);
    }

    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= m; j++) {
            d[i][j] = map[i - 1][j - 1] - '0';
        }
    }

    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= m; j++) {
            if(d[i][j] == 0) continue;

            int dd = d[i - 1][j - 1];
            if(dd > d[i - 1][j]) dd = d[i - 1][j];
            if(dd > d[i][j - 1]) dd = d[i][j - 1];
            
            d[i][j] = dd + 1;

            if(res < d[i][j]) res = d[i][j];
        }
    }

    printf("%d", res * res);

    return 0;
}

'''
