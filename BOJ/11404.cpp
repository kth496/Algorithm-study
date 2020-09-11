#include <bits/stdc++.h>

#define NON_SUBMIT
#ifdef NON_SUBMIT
#define TEST(n) (n)
#define tout cerr
#else
#define TEST(n) ((void)0)
#define tout cin
#endif

#define INF 987654321
using namespace std;
int n, m;

void floyd(vector<vector<int>>& board) {
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == j)
                    board[i][i] = 0;
                else
                    board[i][j] = min(board[i][j], board[i][k] + board[k][j]);
            }
        }
    }
}

int main() {
    TEST(freopen("input.txt", "r", stdin));
    TEST(freopen("output.txt", "w", stdout));
    TEST(freopen("debug.txt", "w", stderr));
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    vector<vector<int>> adj(n + 1, vector<int>(n + 1, INF));
    while (m--) {
        int a, b, c;
        cin >> a >> b >> c;
        adj[a][b] = min(adj[a][b], c);
    }

    floyd(adj);

    for (int r = 1; r <= n; r++) {
        for (int c = 1; c <= n; c++) {
            if (adj[r][c] == INF)
                cout << 0 << " ";
            else
                cout << adj[r][c] << " ";
        }
        cout << '\n';
    }
}
