#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<long long> solution(long long k, vector<long long> room_number) {
    vector<long long> answer;
    long long minn = 1;
    // vector<bool> isFree(k + 1, true);
    long long notFree = 0;
    for (auto e : room_number) {
        if (!(notFree & (1 << e))) {
            notFree |= (1 << e);
            answer.push_back(e);
        } else {
            for (long long i = e + 1;; i++) {
                if (isFree[i]) {
                    isFree[i] = false;
                    answer.push_back(i);
                    break;
                }
            }
        }
    }
    return answer;
}

int main() {
    vector<long long> t1 = {6, 10, 5, 4, 3, 2};
    t1 = solution(10, t1);
    for (auto e : t1) {
        cout << e << " ";
    }
}