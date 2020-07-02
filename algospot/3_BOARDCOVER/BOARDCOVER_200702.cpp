#include <bits/stdc++.h>
using namespace std;

/*
왼쪽 상단 기준으로 채워나가면? 블럭은 3종류
 0
00

 0
 00

 00
  0
 */
int dy[][3] = {{0, 1, 1}, {0, 1, 1}, {0, 0, 1}};
int dx[][3] = {{0, 0, -1}, {0, 0, 1}, {0, 1, 1}};

vector<string> board(23);
int tc, H, W;

bool canCover(int r, int c, int type) {}

void cover(int r, int c, int type, int fill) {}

int solve(int r, int c) {
    if (r == H - 1 && c == W - 1 && board[r][c] == '#') return 1;
    if (board[r][c] == '#') return solve(r + 1, (c + 1) % W);
    int ret = 0;
    for (int _r = r; r < H; r++) {
        for (int _c = c; c < W; c++) {
            for (int t = 0; t < 3; t++) {
                if (canCover(_r, _c, t)) {
                    cover(_r, _c, t, 1);
                    solve(_r + 1, (_c + 1) % W);
                    cover(_r, _c, t, -1);
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string tmp;
    cin >> tc;
    while (tc--) {
        cin >> H >> W;
        for (int i = 0; i < H; i++) {
            cin >> board[i];
        }
    }
}