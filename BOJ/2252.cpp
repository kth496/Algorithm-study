#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<int> height[32001];
bool isVisited[32001];
vector<int> ans;

void dfs(int node) {
    if (height[node].size() == 0) {
        ans.push_back(node);
        return;
    }

    for (int next : height[node]) {
        if (!isVisited[next]) {
            isVisited[next] = true;
            dfs(next);
        }
    }
    ans.push_back(node);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    int a, b;
    while (M--) {
        cin >> a >> b;
        height[a].push_back(b);
    }

    for (int i = 1; i <= N; i++) {
        if (!isVisited[i]) {
            isVisited[i] = true;
            dfs(i);
        }
    }

    reverse(ans.begin(), ans.end());

    for (int e : ans) cout << e << " ";
}
