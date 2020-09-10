#include <bits/stdc++.h>

using namespace std;

struct Trie {
    Trie *nextNode[30];
    bool isFinished;

    Trie() {
        fill(nextNode, nextNode + 30, nullptr);
        isFinished = false;
    }

    void insert(char *key) {
        if (*key == '\0') {
            isFinished = true;
            return;
        }

        int nextIdx = *key - 'a';
        if (!nextNode[nextIdx]) nextNode[nextIdx] = new Trie;
        nextNode[nextIdx]->insert(key + 1);
    }
};

bool find(Trie *trie, char *key) {
    if (*key == '\0') return trie->isFinished;

    int curIdx = *key - 'a';
    if (!trie->nextNode[curIdx]) return false;
    return find(trie->nextNode[curIdx], key + 1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, M;
    cin >> N >> M;

    Trie *root = new Trie;
    for (int i = 0; i < N; i++) {
        char s[503];
        cin >> s;
        root->insert(s);
    }

    int ans = 0;
    for (int i = 0; i < M; i++) {
        char s[503];
        cin >> s;
        if (find(root, s)) ans++;
    }
    cout << ans << '\n';
}