#include <bits/stdc++.h>

using namespace std;

int R, C;
int board[301][301];
bool isVisited[301][301];
int dr[] = {0, 0, 1, -1};
int dc[] = {1, -1, 0, 0};

void melt2() {
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            if (board[r][c] != 0) {
                int zeros = 0;
                for (int k = 0; k < 4; k++) {
                    int nr = r + dr[k];
                    int nc = c + dc[k];
                    if (0 <= nr && nr < R && 0 <= nc && nc < C &&
                        board[nr][nc] == 0)
                        zeros++;
                }
                if (board[r][c] - zeros <= 0)
                    board[r][c] = -1;
                else
                    board[r][c] -= zeros;
            }
        }
    }

    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            if (board[r][c] == -1) board[r][c] = 0;
        }
    }
}

int bfs(int r, int c) {
    queue<pair<int, int>> q;
    isVisited[r][c] = true;
    q.push({r, c});
    while (!q.empty()) {
        int r_ = q.front().first;
        int c_ = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nr = r_ + dr[i];
            int nc = c_ + dc[i];
            if (0 <= nr && nr < R && 0 <= nc && nc < C && !isVisited[nr][nc] &&
                board[nr][nc] != 0) {
                isVisited[nr][nc] = true;
                q.push({nr, nc});
            }
        }
    }
    return 1;
}

int count() {
    memset(isVisited, 0, sizeof(isVisited));

    int cnt = 0;
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            if (!isVisited[r][c] && board[r][c] != 0) {
                cnt += bfs(r, c);
            }
        }
    }
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> R >> C;

    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            cin >> board[r][c];
        }
    }

    int year = 0;
    int cnt;
    while (true) {
        melt2();
        year++;
        cnt = count();
        if (cnt == 0) {
            cout << 0 << '\n';
            break;
        } else if (cnt > 1) {
            cout << year << '\n';
            break;
        }
    }
}
