#include <bits/stdc++.h>
using namespace std;

int n;
// (dy, dx)
int moveType[8][2] = {{-1, -1}, {0, -1}, {1, -1}, {1, 0},
                      {1, 1},   {0, 1},  {-1, 1}, {-1, 0}};

// 체스판을 덮는 함수
void setter(vector<vector<int>> &board, int movNum, int y, int x, int delta) {
  // (y, x) 를 칠하고 movNum 규칙에 맞게 다음 칸으로 이동 후 setter 호출
  if (y < 0 || y >= n || x < 0 || x >= n)
    return;
  board[y][x] += delta;
  setter(board, movNum, y + moveType[movNum][0], x + moveType[movNum][1],
         delta);
  return;
}

bool setter2(vector<vector<int>> &board, int movNum, int y, int x, int delta) {
  if (y < 0 || y >= n || x < 0 || x >= n)
    return true;
  if (board[y][x] = !0) {
    return false;
  }
}

// 왼쪽 상단부터 빈칸을 찾아서 하나씩 놓아본다.
int recur(vector<vector<int>> &board, int queens) {
  if (queens == n)
    return 1;

  int y = -1, x = -1;
  int ret = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (board[i][j] == 0) {
        y = i;
        x = j;
        // 보드 칠하기
        board[y][x] += 1;
        for (int c = 0; c < 8; ++c) {
          setter(board, c, y + moveType[c][0], x + moveType[c][1], 1);
        }

        // 재귀호출
        ret += recur(board, queens + 1);

        // 칠했던 보드 복구
        board[y][x] -= 1;
        for (int c = 0; c < 8; ++c) {
          setter(board, c, y + moveType[c][0], x + moveType[c][1], -1);
        }
      }
    }
  }
  if (y == -1) {
    return 0;
  }

  return ret;
}

int main() {
  ios_base ::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> n;
  vector<vector<int>> board(n, vector<int>(n, 0));

  // 내가 만든 recur 함수는 중복의 경우를 모두 세어버린다.
  // 따라서 n!로 나눠줘야 한다.
  int div = 1, tmp = recur(board, 0);
  for (int i = n; i > 1; --i) {
    div *= i;
  }
  cout << tmp / div;
  return 0;
}