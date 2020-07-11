#include <bits/stdc++.h>
#define g(n) (n * (n + 1) / 2)
using namespace std;

int Answer;
int solve(int x) {
    int ret = 0, i = 0;
    for (i = 0;; i++) {
        if (x == 1) return ret + 1;
        if (x == 0) return ret;
        if ((g(i) <= x) && (x < g((i + 1)))) {
            ret += i;
            x -= g(i);
            i = 0;
        }
    }
}

int wrapper(int a, int b) {
    int maxi = 0;
    int tmp = 0;
    for (int i = a; i <= b; i++) {
        maxi = max(maxi, solve(i));
        if (solve(i) == maxi) tmp = i;
    }
    cout << "tmp : " << tmp << '\n';
    return maxi;
}

int main(int argc, char** argv) {
    int T, test_case, a, b;
    cin >> T;
    for (test_case = 0; test_case < T; test_case++) {
        Answer = 0;
        cin >> a >> b;
        Answer = wrapper(a, b);
        cout << "Case #" << test_case + 1 << endl;
        cout << Answer << endl;
    }

    return 0;  // Your program should return 0 on normal termination.
}