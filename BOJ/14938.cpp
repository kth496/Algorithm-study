#include <bits/stdc++.h>
#define INF 987654
using namespace std;

int items[103];
vector<vector<int>> adj(103, vector<int>(103, INF));

int N, M, R;

void floyd() {
    for (int k = 1; k <= N; k++) {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (i == j)
                    adj[i][j] = 0;
                else
                    adj[i][j] = min(adj[i][k] + adj[k][j], adj[i][j]);
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N >> M >> R;

    for (int i = 1; i <= N; i++) cin >> items[i];
    int a, b, val;
    for (int i = 0; i < R; i++) {
        cin >> a >> b >> val;
        adj[a][b] = adj[b][a] = val;
    }

    floyd();

    int ans = 0;
    for (int i = 1; i <= N; i++) {
        int tmp = 0;
        for (int j = 1; j <= N; j++) {
            if (adj[i][j] <= M) tmp += items[j];
        }
        ans = max(ans, tmp);
    }

    cout << ans;
}
