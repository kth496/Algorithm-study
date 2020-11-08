#include <bits/stdc++.h>

using namespace std;

int R, C;
int board[501][501];
int dp[501][501];

int dr[] = {0, 0, 1, -1};
int dc[] = {1, -1, 0, 0};

int search(int r, int c) {
    if (r == R - 1 && c == C - 1) return 1;
    if (dp[r][c] != -1) return dp[r][c];

    dp[r][c] = 0;

    int h = board[r][c];
    for (int i = 0; i < 4; i++) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (0 <= nr && nr < R && 0 <= nc && nc < C) {
            int nxt_h = board[nr][nc];
            if (nxt_h < h) {
                dp[r][c] += search(nr, nc);
            }
        }
    }

    return dp[r][c];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> R >> C;
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++) cin >> board[r][c];
    memset(dp, -1, sizeof(dp));
    cout << search(0, 0);
}
