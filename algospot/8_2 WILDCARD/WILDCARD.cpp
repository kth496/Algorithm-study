#include <bits/stdc++.h>
using namespace std;

int T, N;

bool match(const string& w, const string& s) {}

void solveWrapper(const string& w, vector<string> sset) {
    for (string s : sset)
        if (match(w, s)) cout << s << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> T;
    while (T--) {
        string wildcard;
        vector<string> sset(N);
        cin >> wildcard;
        cin >> N;
        for (int i = 0; i < N; i++) cin >> sset[i];
        solveWrapper(wildcard, sset);
    }
}