#include <bits/stdc++.h>

using namespace std;

int T, N;
int board[2][100003];
int dp[2][100003];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> T;
    while (T--) {
        cin >> N;

        memset(board, 0, sizeof(board));
        memset(dp, 0, sizeof(dp));
        for (int i = 0; i < 2; i++) {
            for (int j = 1; j <= N; j++) {
                cin >> board[i][j];
            }
        }

        dp[0][1] = board[0][1];
        dp[1][1] = board[1][1];

        for (int c = 2; c <= N; c++) {
            dp[0][c] = max(dp[0][c - 1], dp[1][c - 1] + board[0][c]);
            dp[1][c] = max(dp[1][c - 1], dp[0][c - 1] + board[1][c]);
        }

        cout << max(dp[0][N], dp[1][N]) << "\n";
    }
}
