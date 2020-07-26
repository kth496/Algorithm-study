#include <bits/stdc++.h>
#define MAXN 26
using namespace std;

/*
    @ N         : N*N 행렬의 크기를 나타냄
    @ board     : 주택 정보(0 or 1) 을 나타내는 2차원 배열
    @ isVisited : 주택을 방문했는지 나타내는 2차원 배열
*/
int N;
int board[MAXN][MAXN];
bool isVisited[MAXN][MAXN];

/*
    @ cnt    : 단지 수를 나타냄
    @ houses : 각 단지에 속한 주택의 수를 나타냄
*/
int cnt;
vector<int> houses;

void DFS(int r, int c) {
    /* DFS 종료 조건
        1. 이미 방문한 경우
        2. board를 벗어나는 경우
        3. board[r][c] = 0, 즉 주택이 아닌 경우
    */
    if (isVisited[r][c]) return;
    if (r < 0 || r >= N || c < 0 || c >= N) return;
    if (board[r][c] == 0) return;

    isVisited[r][c] = true;
    houses[cnt - 1]++;

    /* 2차원 배열에서 4방향 방문하기
    이거 말고, dy dx배열을 만들어서 for문으로 방문할수도 있다.
    */
    DFS(r + 1, c);
    DFS(r - 1, c);
    DFS(r, c + 1);
    DFS(r, c - 1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    /* 입력을 받아서 board를 초기화하는 부분
    1 0 0 1 이런 형태가 아니라 1001 이런식으로 주어지기 때문에,
    cin으로 바로 처리하지 못해서 string으로 받아온 뒤 int로 변환해서 저장
    이때 아스키코드값을 처리하기 위해 48을 빼야 한다.
    */
    cin >> N;
    string tmp;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        for (int j = 0; j < tmp.length(); j++) board[i][j] = tmp[j] - 48;
    }

    /* board의 특정 지점이 방문한 적 없고, 주택(1)이면 DFS를 시작한다.*/
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++)
            if (!isVisited[r][c] && board[r][c] == 1) {
                cnt++;
                houses.push_back(0);
                DFS(r, c);
            }
    }

    /* 문제의 요구대로 정렬해서 정답 출력 */
    cout << cnt << '\n';
    sort(houses.begin(), houses.end());
    for (int e : houses) cout << e << '\n';
}
