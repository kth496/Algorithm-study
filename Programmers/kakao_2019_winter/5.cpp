#include <iostream>
#include <string>
#include <vector>
#define INF 2100000000
using namespace std;

int solution(vector<int> stones, int k) {
    ios_base::sync_with_stdio(false);
    int answer = INF, maxx, idx;
    int n = stones.size();
    for (int i = 0; i <= n - k;) {
        maxx = 0;
        idx = 1;
        for (int j = i; j < i + k; j++) {
            if (maxx <= stones[j]) {
                idx = j;
                maxx = stones[j];
            }
        }
        i = (idx + 1);
        answer = min(answer, maxx);
    }
    return answer;
}

int main() {
    vector<int> t1 = {2, 4, 5, 3, 2, 1, 4, 2, 5, 1};
    cout << solution(t1, 3);
}