#include <bits/stdc++.h>

using namespace std;

int N, M, K;
int cost[10003];
int link[10003];
int v[10003];

int find(int x) {
    if (x == link[x]) return x;
    return link[x] = find(link[x]);
}

void unite(int a, int b) {
    a = find(a);
    b = find(b);
    if (cost[a] > cost[b]) swap(a, b);
    link[b] = a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M >> K;

    for (int i = 1; i <= N; i++) {
        link[i] = i;
        cin >> cost[i];
    }

    int a, b;
    while (M--) {
        cin >> a >> b;
        unite(a, b);
    }

    int sum = 0;
    for (int i = 1; i <= N; i++) {
        int anc = find(i);
        if (!v[anc]) {
            sum += cost[anc];
            v[anc] = 1;
        }
    }

    if (sum > K)
        cout << "Oh no";
    else
        cout << sum;
}
