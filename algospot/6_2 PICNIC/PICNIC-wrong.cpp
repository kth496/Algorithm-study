#include <bits/stdc++.h>
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

int n, m; // student count, pair count

bool hasFriend(int person_a, int person_b, int remain) {
  //   cout << isFriend[a][b];
}

int printAnswer() {
  int ret = 0;
  for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
      if (hasFriend(i, j, n))
        ret++;
    }
  }
  return ret;
}

int main() {
  ios_base ::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int tc, a, b;

  cin >> tc;
  while (tc--) {
    cin >> n >> m;
    vector<vector<bool>> friendRelation(n, vector<bool>(n, false));
    vector<vector<bool>> isFriend(n, vector<bool>(n, false));
    vector<bool> hasPair(n, false);
    while (m--) {
      cin >> a >> b;
      friendRelation[a][b] = true;
      friendRelation[b][a] = true;
    }
  }
}