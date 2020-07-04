#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> st(5);
    for (int i = 0; i < st.size(); i++) {
        st[i] = i;
    }

    next_permutation(st.begin(), st.end());
}
