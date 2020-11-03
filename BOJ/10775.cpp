#include <bits/stdc++.h>
#define MAXX 1000002
using namespace std;

int G, P, gi;

int link[MAXX];
int size[MAXX];

int find(int x) {
    if (x == link[x]) return x;
    return link[x] = find(link[x]);
}

void unite(int a, int b) {
    a = find(a);
    b = find(b);
    link[b] = a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> G >> P;

    for (int i = 1; i <= G; i++) link[i] = i;

    int cnt = 0;
    vector<int> planes;
    while (P--) {
        cin >> gi;
        planes.push_back(gi);
    }

    for (int& plane : planes) {
        int gate = find(plane);
        if (gate == 0) break;
        unite(gate - 1, gate);
        cnt++;
    }

    cout << cnt;
}
