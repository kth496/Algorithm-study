#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, S, a;
    cin >> N >> S;

    vector<int> arr;
    vector<int> psum;
    int acc = 0;
    psum.push_back(0);

    for (int i = 0; i < N; i++) {
        cin >> a;
        arr.push_back(a);
        psum.push_back(acc + a);
        acc += a;
    }

    int b = 0, e = 0, ans = N + 1;
    int sum = 0;

    while (true) {
        if (b == N or e == N) break;
        sum = psum[e + 1] - psum[b];
        if (sum < S) e++;
        if (sum >= S) {
            ans = min(ans, e - b + 1);
            b++;
        }
    }

    if (ans == N + 1) ans = 0;
    cout << ans;
}
