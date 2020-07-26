#include <bits/stdc++.h>
#define MAXN 1002
using namespace std;

int N, M, V;
int e1, e2;

/* 그래프 구조 및 방문 여부를 저장*/
vector<int> edge[MAXN];
bool isVisited[MAXN];

/* 정답 출력용 */
vector<int> DFS_ans;
vector<int> BFS_ans;

void DFS(int e) {
    if (isVisited[e]) return;
    isVisited[e] = true;
    DFS_ans.push_back(e);
    for (int next : edge[e]) {
        DFS(next);
    }
}

void BFS(int e) {
    queue<int> q;
    q.push(e);
    while (!q.empty()) {
        if (BFS_ans.size() == N) return;
        int e = q.front();
        q.pop();
        if (isVisited[e]) continue;
        isVisited[e] = true;
        BFS_ans.push_back(e);
        for (int next : edge[e])
            if (!isVisited[next]) q.push(next);
    }
}

int main() {
    /* 입력을 받고 초기화하는 부분 */
    cin >> N >> M >> V;
    for (int i = 0; i < M; i++) {
        cin >> e1 >> e2;
        edge[e1].push_back(e2);
        edge[e2].push_back(e1);
    }

    /* 정점 번호가 낮은 순서로 방문해야하므로 정렬한다.*/
    for (auto &edg : edge) sort(edg.begin(), edg.end());

    /* DFS, BFS 탐색 시작*/
    DFS(V);
    memset(isVisited, 0, sizeof(isVisited));
    BFS(V);

    /* 정답 출력 */
    for (int a : DFS_ans) cout << a << " ";
    cout << '\n';
    for (int a : BFS_ans) cout << a << " ";
}