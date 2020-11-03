#include <bits/stdc++.h>
#define INF 100000001
using namespace std;

int N;
int tower[500003];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    vector<int> ans;
    stack<int> st;
    st.push(0);
    tower[0] = INF;

    int cur;
    for (int i = 1; i <= N; i++) {
        cin >> cur;
        tower[i] = cur;
        if (tower[st.top()] <= cur) {
            while (!st.empty()) {
                if (tower[st.top()] > cur) {
                    ans.push_back(st.top());
                    break;
                }
                st.pop();
            }
        } else {
            ans.push_back(st.top());
        }
        st.push(i);
    }
    for (int& e : ans) cout << e << " ";
}
