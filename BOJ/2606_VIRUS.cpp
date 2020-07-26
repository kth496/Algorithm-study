#include <bits/stdc++.h>
#define MAXN 103
using namespace std;

/*
    @ E         : 노드 수(Edge)
    @ V         : 간선 수(Vertex)
    @ ans       : DFS함수가 방문하는 노드의 수를 나타냄
    @ edge      : 그래프 정보 저장(무방향)
    @ isVisited : 방문 여부를 bool형으로 나타냄
*/
int N, M, ans = 0;
vector<int> edge[MAXN];
bool isVisited[MAXN];

void DFS(int e) {
    if (isVisited[e]) return;
    isVisited[e] = true;
    ans++;
    for (int next : edge[e]) DFS(next);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    /* 입력을 바탕으로 그래프 배열인 edge를 초기화함 */
    cin >> N >> M;
    int e1, e2;
    for (int i = 0; i < M; i++) {
        cin >> e1 >> e2;
        edge[e1].push_back(e2);
        edge[e2].push_back(e1);
    }

    /* DFS로 노드 방문 시작 */
    DFS(1);

    /* 정답 출력 */
    cout << ans - 1;
}
