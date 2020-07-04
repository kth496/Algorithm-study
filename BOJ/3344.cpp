#include <bits/stdc++.h>
using namespace std;

// 해결방법
// https://en.wikipedia.org/w/index.php?title=Eight_queens_puzzle&oldid=844460636#Explicit_solutions

void solution(int n) {
    bool isOdd = false;
    if (n % 2) isOdd = true;
    if ((!isOdd && n % 6 != 2) || (isOdd && (n - 1) % 6 != 2)) {
        if (isOdd) n--;
        for (int i = 1; i <= n / 2; i++) printf("%d\n", 2 * i);
        for (int i = 1; i <= n / 2; i++) printf("%d\n", 2 * i - 1);
        if (isOdd) printf("%d\n", n + 1);
    } else if ((!isOdd && n / 6 != 0) || (isOdd && (n - 1) / 6 != 2)) {
        if (isOdd) n--;
        for (int i = 1; i <= n / 2; i++)
            printf("%d\n", 1 + (2 * i + n / 2 - 3) % n);
        for (int i = n / 2; i > 0; i--)
            printf("%d\n", n - (2 * i + n / 2 - 3) % n);
        if (isOdd) printf("%d\n", n + 1);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin >> N;
    solution(N);
}