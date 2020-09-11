// 1865
#include <bits/stdc++.h>
#define MAXX 503
#define INF 987654321
using namespace std;

int N, M, W, TC, S, E, T;

struct edge {
    int dest;
    int val;
};

vector<edge> edge_vec[MAXX];
int arr[MAXX];

int bellman_ford(int excute_num) {
    bool isValid = false;
    for (int t = 1; t <= N; t++) {
        for (int i = 1; i <= N; i++) {
            for (int k = 0; k < edge_vec[i].size(); k++) {
                int new_val = (arr[i] + edge_vec[i][k].val);
                int before_val = (arr[edge_vec[i][k].dest]);
                if ((arr[i] != INF) && (new_val < before_val)) {
                    isValid = true;
                    if (isValid * excute_num) return isValid;
                    arr[edge_vec[i][k].dest] = new_val;
                }
            }
        }
    }
    return isValid;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> TC;
    while (TC--) {
        cin >> N >> M >> W;

        // init
        for (int i = 2; i <= N; i++) arr[i] = INF;
        for (int i = 1; i <= N; i++) edge_vec[i].clear();

        while (M--) {
            cin >> S >> E >> T;
            edge_vec[S].push_back(edge{E, T});
            edge_vec[E].push_back(edge{S, T});
        }

        while (W--) {
            cin >> S >> E >> T;
            edge_vec[S].push_back(edge{E, -T});
        }

        bellman_ford(0);

        bool flag = true;
        if (bellman_ford(1)) {
            {
                cout << "YES" << '\n';
                flag = false;
            }
        } else {
            if (arr[N] == INF) {
                cout << "YES" << '\n';
                flag = false;
            }
        }
        if (flag) cout << "NO" << '\n';
    }
}
