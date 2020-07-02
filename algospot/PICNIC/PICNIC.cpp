// #include <bits/stdc++.h>
#include <iostream>
using namespace std;
/*
3
2 1
0 1
4 6
0 1 1 2 2 3 3 0 0 2 1 3
6 10
0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5
 */
int n, m;
bool areFriends[10][10];

int countPairings(bool taken[10]) {
    int firstFree = -1;
    for (int i = 0; i < n; i++) {
        if (!taken[i]) {
            firstFree = i;
            break;
        }
    }

    if (firstFree == -1) return 1;

    int ret = 0;
    for (int pairWith = firstFree + 1; pairWith < n; ++pairWith)
        if (!taken[pairWith] && areFriends[firstFree][pairWith]) {
            taken[firstFree] = taken[pairWith] = true;
            ret += countPairings(taken);
            taken[firstFree] = taken[pairWith] = false;
        }
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int tc, a, b;
    cin >> tc;
    while (tc--) {
        // initialize taken array
        bool taken[10] = {
            false,
        };
        cin >> n >> m;

        // initialize areFriends array(global variable)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                areFriends[i][j] = false;
            }
        }

        // input areFriends
        while (m--) {
            cin >> a >> b;
            areFriends[a][b] = true;
            areFriends[b][a] = true;
        }
        cout << countPairings(taken) << '\n';
    }
}