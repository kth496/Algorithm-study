#include <bits/stdc++.h>

using namespace std;

struct Trie {
    Trie* next[26];
    bool isEnd;
    int count;
    Trie() {
        fill(next, next + 26, nullptr);
        isEnd = false;
        count = 0;
    }

    void insert(string key) {
        Trie* cNode = this;
        for (int i = 0; i < key.length(); i++) {
            int idx = key[i] - 'a';
            if (!cNode->next[idx]) cNode->next[idx] = new Trie;
            cNode->count++;
            cNode = cNode->next[idx];
        }
        cNode->isEnd = true;
    }

    int find(char* key, Trie* node) {
        if (*key == '\0') {
            if (node->isEnd)
                return 1;
            else
                return 0;
        }

        int ret = 0;

        if (*key == '?') {
            // for (int i = 0; i < 26; i++) {
            //     if (node->next[i]) {
            //         ret += find(key + 1, node->next[i]);
            //     }
            // }
            ret += node->count;
        } else {
            int idx = *key - 'a';
            if (!node->next[idx])
                return 0;
            else {
                ret += find(key + 1, node->next[idx]);
            }
        }

        return ret;
    }
};

vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer;
    Trie* tlist[100001];
    Trie* rtlist[100001];
    Trie* root = new Trie;
    Trie* root_rev = new Trie;

    for (string word : words) {
        int L = word.length();
        if (!tlist[L]) {
            tlist[L] = new Trie;
            rtlist[L] = new Trie;
        }

        root = tlist[L];
        root_rev = rtlist[L];

        root->insert(word);
        reverse(word.begin(), word.end());
        root_rev->insert(word);
    }

    for (string given : queries) {
        char a[10003];
        int ret;
        if (given[0] == '?') {
            reverse(given.begin(), given.end());
            strcpy(a, given.c_str());
            if (!rtlist[given.length()]) {
                ret = 0;
            } else {
                root_rev = rtlist[given.length()];
                ret = root_rev->find(a, root_rev);
            }
        } else {
            strcpy(a, given.c_str());
            if (!tlist[given.length()]) {
                ret = 0;
            } else {
                root = tlist[given.length()];
                ret = root->find(a, root);
            }
        }
        answer.push_back(ret);
    }
    return answer;
}

int main() {
    vector<string> words = {"frodo",  "front", "frost",
                            "frozen", "frame", "kakao"};

    vector<string> queries = {"?????", "??????????", "?"};
    vector<int> ans;
    ans = solution(words, queries);
    cout << 'n';
}
