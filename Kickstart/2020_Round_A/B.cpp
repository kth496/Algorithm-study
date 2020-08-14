/*
완전히 똑같은 논리로 풀었는데, 파이썬은 시간초과나고 cpp는 통과한다.
파이썬의 입출력 시간에 대한 고민을 해봐야할듯
*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int N, K, P;
        cin >> N >> K >> P;
        vector<vector<int>> dp(N + 1, vector<int>(P + 1));
        vector<vector<int>> st(N, vector<int>(K + 1));
        vector<vector<int>> psum(N, vector<int>(K + 1));
        for (int i = 0; i < N; i++) {
            for (int j = 1; j <= K; j++) {
                cin >> st[i][j];
                psum[i][j] = psum[i][j - 1] + st[i][j];
            }
        }
        for (int i = 1; i < N + 1; i++) {
            for (int j = 1; j < P + 1; j++) {
                for (int x = 0; x < min(j + 1, K + 1); x++) {
                    dp[i][j] = max(psum[i - 1][x] + dp[i - 1][j - x], dp[i][j]);
                }
            }
        }
        cout << "Case #" << tc << ": " << dp[N][P] << '\n';
    }
}