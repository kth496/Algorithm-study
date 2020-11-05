#include <bits/stdc++.h>

using namespace std;

int N;
int arr[101];
int v[101];
int chk[101];
int ans;

bool isCycle(int st, int cur) {
    if (v[cur]) return false;
    v[cur] = 1;

    if (st == cur || isCycle(st, arr[cur])) {
        ans++;
        chk[cur] = 1;
        return true;
    }
    
    v[cur] = 0;
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    for (int i = 1; i <= N; i++) cin >> arr[i];

    for (int i = 1; i <= N; i++) {
        if (!v[i]) isCycle(i, arr[i]);
    }

    cout << ans << '\n';
    for (int i = 1; i <= N; i++)
        if (chk[i]) cout << i << '\n';
}
