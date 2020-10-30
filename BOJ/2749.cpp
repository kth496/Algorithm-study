#include <bits/stdc++.h>

using namespace std;

const int M = 1000000;
const int P = M / 10 * 15;
int fib[P + 3] = {0, 1};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    long long target;
    cin >> target;

    for (int i = 2; i < P; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
        fib[i] %= M;
    }

    target = target % P;
    cout << fib[target] << '\n';
}
