#include <bits/stdc++.h>
using namespace std;
/*
3
3 7
#.....#
#.....#
##...##
3 7
#.....#
#.....#
##..###
8 10
##########
#........#
#........#
#........#
#........#
#........#
#........#
##########
*/
int r, c;
const int coverType[4][3][2] = {{{0, 0}, {1, 0}, {0, 1}},
                                {{0, 0}, {0, 1}, {1, 1}},
                                {{0, 0}, {1, 0}, {1, 1}},
                                {{0, 0}, {1, 0}, {1, -1}}};

int recur(int y, int x, string field[20]) {
    if (y == r - 1, x == c - 1) return 1;
    int ret = 0;
    for (int i = y; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (field[y][x] == '.') {  // 여기서 블록을 내려놓는다
                for (auto moving : coverType) {
                    bool inField = true;
                    for (int i = 0; i < 3; i++) {
                        int dy = moving[i][0];
                        int dx = moving[i][1];
                        if ((y + dy > 0 && y + dy < r && x + dx > 0 &&
                             x + dx < c) == false) {
                            inField = false;
                            break;
                        }
                        if ((field[y + dy][x + dx] == '#')) inField = false;
                    }
                    if (inField) {
                    }
                }
            }
        }
    }
}

int main() {
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int tc;
    while (tc--) {
        string field[20];
        cin >> r >> c;

        for (int i = 0; i < r; i++) {
            string tmp;
            cin >> tmp;
            field[i] = tmp;
        }
        cout << recur(0, 0, field) << '\n';
    }
}