#include <bits/stdc++.h>

using namespace std;

unordered_map<string, pair<string, int>> mp;  // 부모문자열, 사이즈를 저장함.

// 유니온 파인드로 해결하자. find 함수와 unite함수를 구현한다.

// 인자로 받아온 s가 속한 집합의 최상위 부모 문자열을 리턴함
string find(string s) {
    if (!mp.count(s)) {  // 맵에 이름이 없으면 새로 만든다.
        mp[s] = {s, 1};
        return s;
    }
    if (s == mp[s].first) return s;
    return mp[s].first = find(mp[s].first);  // 경로압축함
}

// s1, s2의 집합을 합친다. 합친 후 집합의 크기를 리턴함
int unite(string s1, string s2) {
    s1 = find(s1);
    s2 = find(s2);
    // 같은 집합에 속한 경우를 처리하지 않아서 오래 고민했다.
    if (s1 == s2) return mp[s1].second;

    if (mp[s1].second < mp[s2].second) swap(s1, s2);
    mp[s1].second += mp[s2].second;
    mp[s2].first = s1;

    return mp[s1].second;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, m;
    cin >> t;
    while (t--) {
        mp.clear();  // 각 테스트케이스 시작마다 맵을 비운다.
        cin >> m;
        string s1, s2;  // 입력으로 받을 사람 이름 2개
        while (m--) {
            // 입력받고 합쳐서 결과를 출력한다. unite함수 참고
            cin >> s1 >> s2;
            cout << unite(s1, s2) << '\n';
        }
    }
}

/*
1
4
a b
a c
d e
d c

*/
