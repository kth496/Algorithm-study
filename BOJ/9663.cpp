#include <bits/stdc++.h>
using namespace std;

int N, count_;
bool already = false;

bool isValid(vector<int>& queens, int k) {
    int i = 0;
    while (i < k) {
        if (queens[k] == queens[i] || abs(queens[k] - queens[i]) == k - i)
            return false;
        i++;
    }
    return true;
}

void printAns(vector<int> ans) {
    for (auto e : ans) {
        cout << e << " ";
    }
}

void nqueen(vector<int> queens) {
    bool findAns = false;
    for (int i = 0; i < N; i++) {
        queens.push_back(i);
        if (isValid(queens, queens.size() - 1)) {
            if (queens.size() == N) {
                if (!already) {
                    printAns(queens);
                    already = true;
                }
                count_++;
                return;
            }
            nqueen(queens);
        }
        queens.pop_back();
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    vector<int> init(0);
    nqueen(init);
    // cout << count_;
}