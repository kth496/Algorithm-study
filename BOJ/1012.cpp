#include <bits/stdc++.h>
using namespace std;

int tc, M, N, K, b, a;

// dy, dx
int mov[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

bool inBoard(int y, int x) {
    if (y < 0 || y >= N || x < 0 || x >= M) return false;
    return true;
}

void placeBug(vector<vector<int>>& board, int y, int x) {
    if (inBoard(y, x) && board[y][x] == 1) {
        board[y][x] = 0;
        for (int e = 0; e < 4; e++) {
            placeBug(board, y + mov[e][0], x + mov[e][1]);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> tc;
    while (tc--) {
        // init
        cin >> M >> N >> K;
        vector<vector<int>> board(N, vector<int>(M, 0));
        while (K--) {
            cin >> a >> b;
            board[b][a] = 1;
        }

        int bug = 0;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (board[y][x] == 1) {
                    placeBug(board, y, x);
                    bug++;
                }
            }
        }
        cout << bug << '\n';
    }
}