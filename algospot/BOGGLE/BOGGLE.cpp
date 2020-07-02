#include <bits/stdc++.h>
using namespace std;

const int dx[8] = {0, 0, 1, 1, 1, -1, -1, -1};
const int dy[8] = {1, -1, 0, 1, -1, 0, 1, -1};

int tc, targetCount;
vector<string> board, target;
string tmp;

bool inRange(int y, int x) {
    return (y < 0 || y > 4 || x < 0 || x > 4) ? false : true;
}

bool hasWord(int y, int x, string word) {
    if (!inRange(y, x)) return false;
    if (word[0] != board[y][x]) return false;
    if (word.size() == 1) return true;
    for (int direction = 0; direction < 8; direction++) {
        int nextY = y + dy[direction], nextX = x + dx[direction];
        if (hasWord(nextY, nextX, word.substr(1))) return true;
    }
    return false;
}

void printAnswer(string curWord) {
    for (int y = 0; y < 5; y++) {
        for (int x = 0; x < 5; x++) {
            if (hasWord(y, x, curWord)) {
                cout << curWord << " YES\n";
                return;
            }
        }
    }
    cout << curWord << " NO\n";
}

int main() {
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    scanf("%d", &tc);
    for (int i = 0; i < 5; i++) {
        cin >> tmp;
        board.push_back(tmp);
    }
    scanf("%d", &targetCount);
    for (int i = 0; i < targetCount; i++) {
        cin >> tmp;
        target.push_back(tmp);
    }

    for (string curWord : target) {
        printAnswer(curWord);
    }
}
