// 4358
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string s;
    int i = 0;
    map<string, double> mp;
    while (getline(cin, s)) {
        mp[s]++;
        i++;
    }

    // fixed 로 소수점 자리수를 고정하고, precision으로 4자리로 지정
    cout << fixed;
    cout.precision(4);

    for (auto it = mp.begin(); it != mp.end(); it++) {
        cout << it->first << " ";
        double ret = it->second;
        cout << ret * 100 / i << '\n';
    }
}
