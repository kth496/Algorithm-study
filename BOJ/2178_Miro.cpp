#include <bits/stdc++.h>
#define MAXN 103
using namespace std;

/*
    @ N, M      : N행 M열의 입력 크기를 나타냄
    @ board     : '1' 또는 '0'의 값을 가지는 2차원 char 배열, '1'로만 이동 가능
    @ cnt       : BFS로 해당 위치를 탐색하는 경로의 길이를 나타냄
*/
int N, M;
char board[MAXN][MAXN];
int cnt[MAXN][MAXN];

/*
4방향 이동을 위한 dr, dc 배열
*/
int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

int BFS(int r, int c) {
    /*
        @ q : (r, c) 를 담아서 BFS를 수행하는 큐
    */
    queue<pair<int, int>> q;
    pair<int, int> e = make_pair(r, c);
    q.push(e);

    /* BFS 시작 */
    while (!q.empty()) {
        e = q.front();
        q.pop();
        int r = e.first, c = e.second;

        /* BFS 탈출 조건 */
        if (r == N - 1 && c == M - 1) return cnt[r][c] + 1;

        /* for문으로 4방향 이동한다.
        아래 if문은 유효한 범위인지와 '1'인지(이동가능한지) 체크한다.
        */
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i], nc = c + dc[i];
            if (board[nr][nc] == '1' &&
                !(nr < 0 || nr >= N || nc < 0 || nc >= M)) {
                /* 이동할때는 이미 지나온 길을 '0'으로 표시하고,
                지나온 길까지의 경로 길이 + 1을 새로운 경로에 기록한다.
                마지막으로, 새로운 좌표인 nr, nc를 큐에 삽입
                */
                board[nr][nc] = '0';
                cnt[nr][nc] = cnt[r][c] + 1;
                q.push(make_pair(nr, nc));
            }
            `
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    string tmp;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        for (int j = 0; j < M; j++) board[i][j] = (char)tmp[j];
    }

    cout << BFS(0, 0);
}