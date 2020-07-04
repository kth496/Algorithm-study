#include <bits/stdc++.h>
using namespace std;

vector<int> x;
vector<bool> isChked;
int N, M;

void printAns(vector<int> s) {
    for (int e : s) cout << e << ' ';
    cout << '\n';
}

void permutation(vector<int> s, int k) {
    if (k == M) {
        printAns(s);
        return;
    }

    int smallest = s.empty() ? 1 : s.back() + 1;
    for (int next = smallest; next <= N; next++) {
        s.push_back(next);
        permutation(s, k + 1);
        s.pop_back();
    }
}

int main() {
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N >> M;

    for (int i = 1; i <= N; i++) {
        x.push_back(i);
        isChked.push_back(false);
    }
    vector<int> ans;
    permutation(ans, 0);
}