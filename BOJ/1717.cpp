#include <bits/stdc++.h>

using namespace std;

int link[1000003];
int siz[1000003];

int find(int x) {
    if (x == link[x]) return x;
    return link[x] = find(link[x]);
}

void unite(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;
    if (siz[a] < siz[b]) swap(a, b);
    siz[a] += siz[b];
    link[b] = a;
}

bool same(int a, int b) { return find(a) == find(b); }

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, M, cmd, a, b;
    cin >> N >> M;
    for (int i = 0; i <= N; i++) link[i] = i;
    for (int i = 0; i <= N; i++) siz[i] = 1;
    for (int i = 0; i < M; i++) {
        cin >> cmd >> a >> b;
        if (cmd == 0)
            unite(a, b);
        else {
            if (same(a, b))
                cout << "YES" << '\n';
            else
                cout << "NO" << '\n';
        }
    }
}