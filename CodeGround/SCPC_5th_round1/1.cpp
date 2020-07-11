#include <iostream>
using namespace std;

int Answer;
int dp[1000001];
int sum_N[1000001];

int search(int n) {
    int& ret = dp[n];
    if (ret != 0) return ret;
    if (n % 2)
        ret = search(n + 1) + 1;
    else
        ret = search(n / 2) + 1;
    return ret;
}

int main(int argc, char** argv) {
    int T, test_case, n1, n2;
    dp[2] = 1;

    for (int i = 2; i < 1000001; i++) sum_N[i] = sum_N[i - 1] + search(i);

    cin >> T;
    for (test_case = 1; test_case <= T; test_case++) {
        cin >> n1 >> n2;
        Answer = sum_N[n2] - sum_N[n1 - 1];

        cout << "Case #" << test_case << "\n" << Answer << "\n";
    }

    return 0;
}
