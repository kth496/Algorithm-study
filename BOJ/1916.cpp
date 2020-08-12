#include <bits/stdc++.h>
#define INF 99999999
using namespace std;

/*
    다익스트라 알고리즘을 사용해 해결할 수 있다.
    그래프의 정보는 연결리스트의 형태로 저장한다.
    adj[a] = {b, w} 꼴로, a노드에서 b노드로 이어진 간선의 가중치가 w임을
   의미한다.

 */
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    /*
    N : 정점의 수
    M : 간선의 수
    a, b, w : 입력받기위한 변수
    st, ed : 출발 도착 위치
    */
    int N, M, a, b, w, st, ed;
    cin >> N >> M;
    vector<vector<pair<int, int>>> adj(N + 1);
    for (int m = 0; m < M; m++) {
        cin >> a >> b >> w;
        adj[a].push_back({b, w});
        // adj[b].push_back({a, w});  // 이 부분에서 틀렸다.
        // 문제 조건상, 왕복 버스가 아니기 때문에 adj에 편도선만 추가해야한다.
    }
    cin >> st >> ed;

    /* 다익스트라 알고리즘 시작 */
    /*
    pq는 우선순위 큐, dist는 st에서 모든 정점까지의 최단거리를 저장함
    v에는 이미 방문했는지 여부를 저장함.
    */

    /*
    Q1. pq에서 pair를 쓰면 어떤 순서로 내부에서 정렬되나?
    -> pair의 first를 먼저 보고, 같으면 second를 본다

    Q2. 디버거에 나와있는 큐의 순서는 영향이 없는걸까?
    -> 그렇다. 알아서 잘 나온다.

    트릭 :
    원래 우선순위 큐는 기본적으로 less<> 가 비교연산자로 설정됨. 즉, 값이
    큰거부터 나온다. 하지만 최단거리를 구할때는 값이 작은것부터 뽑아야한다.
    이때, greater<>로 변경해서 사용하면 pq선언이 너무 길어진다.
    대신 pq에 저장할 때 pair의 first인 거리값에 -를 붙여주면 같은 효과를 얻을 수
    있다.
     */
    priority_queue<pair<int, int>> pq;
    vector<int> dist(N + 1, INF);
    vector<bool> v(N + 1, false);
    dist[st] = 0;
    pq.push({0, st});
    while (!pq.empty()) {
        int a = pq.top().second;
        pq.pop();
        if (v[a]) continue;
        v[a] = true;
        for (auto u : adj[a]) {
            int b = u.first, w = u.second;
            if (dist[a] + w < dist[b]) {
                dist[b] = dist[a] + w;
                pq.push({-dist[b], b});
            }
        }
    }
    cout << dist[ed] << '\n';
}