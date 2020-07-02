#include <bits/stdc++.h>
using namespace std;

string solve(string::iterator &it) {
  char head = *(it++);
  if (head == 'b' || head == 'w')
    return string(1, head);

  string UL = solve(it);
  string UR = solve(it);
  string LL = solve(it);
  string LR = solve(it);
  return string("x") + LL + LR + UL + UR;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int tc;
  cin >> tc;
  while (tc--) {
    string target;
    cin >> target;
    string::iterator start = target.begin();
    cout << solve(start) << '\n';
  }
}
