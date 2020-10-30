#include <bits/stdc++.h>
#define INF 987654321
using namespace std;

int N, M, K, X;
vector<int> adj[300002];
int dist[300002];
bool isVisited[300002];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N >> M >> K >> X;

    while (M--) {
        int st, ed;
        cin >> st >> ed;
        adj[st].push_back(ed);
    }

    for (int i = 1; i <= N; i++) {
        dist[i] = INF;
    }

    priority_queue<pair<int, int>> q;
    dist[X] = 0;
    q.push({0, X});

    while (!q.empty()) {
        int node = q.top().second;
        q.pop();
        if (isVisited[node]) continue;
        isVisited[node] = true;
        for (auto u : adj[node]) {
            if (dist[node] + 1 < dist[u]) {
                dist[u] = dist[node] + 1;
                q.push({-dist[u], u});
            }
        }
    }

    vector<int> ans;

    for (int i = 1; i <= N; i++) {
        if (i != X && dist[i] == K) ans.push_back(i);
    }

    if (ans.size() == 0)
        cout << -1 << '\n';
    else {
        sort(ans.begin(), ans.end());
        for (auto e : ans) cout << e << '\n';
    }
}
