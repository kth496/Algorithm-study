#include <cstring>  // memset
#include <iostream>
using namespace std;

int T, N;
int cache[101][101], board[101][101];

int jump(int y, int x) {
    if (y >= N || x >= N || y < 0 || x < 0) return 0;
    if (y == N - 1 && x == N - 1) return 1;
    int& ret = cache[y][x];
    if (ret != -1) return ret;
    int jumpsize = board[y][x];
    return ret = (jump(y + jumpsize, x) || jump(y, x + jumpsize));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> T;
    while (T--) {
        cin >> N;
        memset(cache, -1, sizeof(cache));
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++) cin >> board[i][j];
        if (jump(0, 0))
            cout << "YES" << '\n';
        else
            cout << "NO" << '\n';
    }
}