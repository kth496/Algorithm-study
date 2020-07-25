#include <bits/stdc++.h>
#define MAX_SIZE 10
using namespace std;

int board[MAX_SIZE][MAX_SIZE];
int Row[MAX_SIZE][MAX_SIZE];
int Col[MAX_SIZE][MAX_SIZE];
int Square[MAX_SIZE][MAX_SIZE];

void printer() {
    for (int y = 0; y < 9; y++) {
        for (int x = 0; x < 9; x++) {
            cout << board[y][x] << " ";
        }
        cout << '\n';
    }
}

void solve(int filled) {
    if (filled == 81) {
        printer();
        exit(0);
    }
    int x = filled % 9, y = filled / 9;
    int SqN = (y / 3) * 3 + (x / 3);
    if (board[y][x] == 0) {
        for (int i = 1; i < 10; i++) {
            if (!Row[y][i] && !Col[x][i] && !Square[SqN][i]) {
                Row[y][i] = 1;
                Col[x][i] = 1;
                Square[SqN][i] = 1;
                board[y][x] = i;
                solve(filled + 1);
                board[y][x] = 0;
                Square[SqN][i] = 0;
                Col[x][i] = 0;
                Row[y][i] = 0;
            }
        }
    } else
        solve(filled + 1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    for (int i = 0; i < 9; i++)
        for (int j = 0; j < 9; j++) {
            cin >> board[i][j];
            if (board[i][j] != 0) {
                Row[i][board[i][j]] = Col[j][board[i][j]] = 1;
                Square[(i / 3) * 3 + (j / 3)][board[i][j]] = 1;
            }
        }
    solve(0);
}
