#include <bits/stdc++.h>
using namespace std;

int N, M;
string tmp;

int solve(vector<string>& board, int y, int x) {
    int cx = 0, cy = 0, ci = 0;
    char c[] = {'W', 'B'};
    int ret = 0;
    while (1) {
        if (board[cy + y][cx + x] != c[ci]) ret++;
        ci = (ci + 1) % 2;
        cx++;
        if (cy == 7 && cx == 8) break;
        if (cx == 8) {
            cy++;
            cx = 0;
            ci = cy % 2;
        }
    }

    int ret2 = 0;
    cx = 0;
    cy = 0;
    ci = 1;
    while (1) {
        if (board[cy + y][cx + x] != c[ci]) ret2++;
        ci = (ci + 1) % 2;
        cx++;
        if (cy == 7 && cx == 8) break;
        if (cx == 8) {
            cy++;
            cx = 0;
            ci = (cy + 1) % 2;
        }
    }
    return min(ret, ret2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    vector<string> board;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        board.push_back(tmp);
    }

    int ret = 99999;
    for (int y = 0; y <= N - 8; y++) {
        for (int x = 0; x <= M - 8; x++) {
            ret = min(ret, solve(board, y, x));
        }
    }
    cout << ret;
}
