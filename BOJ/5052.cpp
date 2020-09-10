// 5052
#include <bits/stdc++.h>

using namespace std;

struct Trie {
    Trie* nextNode[10];
    bool isEnd;
    Trie() {
        fill(nextNode, nextNode + 10, nullptr);
        isEnd = false;
    }

    bool insert(char* key) {
        if (*key == '\0') {
            isEnd = true;
            return true;  // 겹치지 않게 잘 추가함
        }

        int nextIdx = *key - '0';

        // 노드가 없으면 새로 만든다.
        if (!nextNode[nextIdx]) nextNode[nextIdx] = new Trie;

        // 이미 접두사면 삽입 불가
        if (nextNode[nextIdx]->isEnd) return false;

        return nextNode[nextIdx]->insert(key + 1);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        vector<string> list;
        for (int j = 0; j < n; j++) {
            string s;
            cin >> s;
            list.push_back(s);
        }

        // 전화번호의 길이 기준으로 오름차순 정렬
        sort(list.begin(), list.end(), [](const string& s1, const string& s2) {
            return s1.size() < s2.size();
        });

        Trie* root = new Trie();
        bool flag = true;

        for (int j = 0; j < n; j++) {
            char a[11];
            strcpy(a, list[j].c_str());
            if (!root->insert(a)) {
                flag = false;
                break;
            }
        }

        if (flag)
            cout << "YES" << '\n';
        else
            cout << "NO" << '\n';
    }
}
