#include <bits/stdc++.h>
#define INF 87654321
using namespace std;
/*
2
12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12
12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6
*/
const string linked[10] = {"xxx.............", "...x...x.x.x....",
                           "....x.....x...xx", "x...xxxx........",
                           "......xxx.x.x...", "x.x...........xx",
                           "...x..........xx", "....xx.x......xx",
                           ".xxxxx..........", "...xxx...x...x.."};

// 12 3 6 9
bool areAligned(const vector<int> &clocks) {
  for (int eachClock : clocks) {
    if (eachClock != 12)
      return false;
  }
  return true;
}

// switch번 스위치를 누른다.
void push(vector<int> &clocks, int _switch) {
  for (int clock = 0; clock < 16; clock++)
    if (linked[_switch][clock] == 'x') {
      clocks[clock] += 3;
      if (clocks[clock] == 15)
        clocks[clock] = 3;
    }
}

int solve(vector<int> &clocks, int _switch) {
  if (_switch == 10)
    return areAligned(clocks) ? 0 : INF;

  int ret = INF;
  for (int i = 0; i < 4; i++) {
    ret = min(ret, i + solve(clocks, _switch + 1));
    push(clocks, _switch);
  }
  return ret;
}

int main() {
  int tc, tmp;
  ios_base ::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> tc;
  while (tc--) {
    vector<int> initState(16, 0);
    for (int i = 0; i < 16; i++) {
      cin >> tmp;
      initState[i] = tmp;
    }
    // for (int i = 0; i < 8; i++) {
    //   int a;
    //   cin >> a;
    //   push(initState, a);
    // }

    int a = solve(initState, 0);
    if (a == INF)
      a = -1;
    cout << a << '\n';
  }
}