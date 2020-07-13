#include <bits/stdc++.h>

using namespace std;

int Answer, l, r, N, a, b;
vector<pair<long long, long long>> impure;

long long solve() {
    long long ret = 0, pret, xi, yi, Lxi, Lyi, Di;
    for (int i = l; i <= r; i++) {
        pret = 99999999999;
        for (auto e : impure) {
            xi = e.first;
            yi = e.second;
            Lxi = abs(xi - i);
            Lyi = abs(yi);
            Di = max(Lxi, Lyi);
            pret = min(pret, Di);
        }
        ret = max(ret, pret);
    }
    return 2 * ret;
}

long long solve2() { long long Lyi; }

int main(int argc, char** argv) {
    int T, test_case;

    cin >> T;
    for (test_case = 0; test_case < T; test_case++) {
        Answer = 0;

        cin >> l >> r;
        cin >> N;

        for (int i = 0; i < N; i++) {
            cin >> a >> b;
            pair<int, int> tmp = make_pair(a, b);
            impure.push_back(tmp);
        }

        Answer = solve();

        cout << "Case #" << test_case + 1 << endl;
        cout << Answer << endl;
    }

    return 0;  // Your program should return 0 on normal termination.
}