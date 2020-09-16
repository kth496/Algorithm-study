#include <bits/stdc++.h>
#define INF 987654321
#define int int64_t
using namespace std;

main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, M;
    cin >> N >> M;

    // init
    vector<vector<int>> board(N + 1, vector<int>(N + 1, INF));
    vector<int> dist(N + 1, INF);
    vector<bool> processed(N + 1);
    vector<int> path(N + 1);

    // input
    for (int i = 0; i < M; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        board[a][b] = min(board[a][b], c);
    }

    // start, arrival
    int st, ar;
    cin >> st >> ar;

    priority_queue<pair<int, int>> pq;

    dist[st] = 0;
    pq.push({0, st});
    while (!pq.empty()) {
        int a = pq.top().second;
        pq.pop();
        if (processed[a]) continue;
        processed[a] = true;
        for (int next = 1; next <= N; next++) {
            int route = board[a][next];
            if (route != INF) {
                if (dist[a] + route < dist[next]) {
                    path[next] = a;
                    dist[next] = dist[a] + route;
                    pq.push({-dist[next], next});
                }
            }
        }
    }

    // output
    vector<int> find;
    int node = ar;
    while (true) {
        if (node == 0) break;
        find.push_back(node);
        node = path[node];
    }
    reverse(find.begin(), find.end());
    cout << dist[ar] << '\n' << find.size() << '\n';
    for (auto e : find) cout << e << " ";
    cout << '\n';
}
