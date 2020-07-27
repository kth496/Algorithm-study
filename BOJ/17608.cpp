#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, a;
    cin >> N;
    vector<int> d(N);
    for (int i = 0; i < N; i++) cin >> d[i];

    int key = d[N - 1], ans = 0;
    for (int i = N - 2; i > -1; i--) {
        if (d[i] > key) {
            ans++;
            key = d[i];
        }
    }
    cout << ans + 1;
}