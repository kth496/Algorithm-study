#include <bits/stdc++.h>
#define MAXX 4000000
using namespace std;

int chked[MAXX];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int last = 0;
    int N;
    cin >> N;

    vector<int> primes;
    vector<int> psum;
    psum.push_back(0);

    for (int i = 2; i <= MAXX; i++) {
        if (chked[i] == 0) {
            last += i;
            primes.push_back(i);
            psum.push_back(last);
            for (int j = i * 2; j <= MAXX; j += i) {
                chked[j] = 1;
            }
        }
    }

    int cnt = 0, sum = 0;
    int f = 0, e = 0;
    while (true) {
        if (f == primes.size()) break;
        if (sum == N) cnt++;
        if (sum >= N) f++;
        if (sum < N) e++;
        sum = psum[e] - psum[f];
    }
    cout << cnt;
}
