#include <bits/stdc++.h>

using namespace std;

int N;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int line_1[3];
    int line_2[3];
    int line_3[3];
    int line_min[3];

    cin >> N;
    cin >> line_1[0] >> line_1[1] >> line_1[2];

    copy(line_1, line_1 + 3, line_3);
    copy(line_1, line_1 + 3, line_min);

    N--;
    while (N--) {
        cin >> line_2[0] >> line_2[1] >> line_2[2];

        swap(line_1, line_3);
        line_3[0] = max(line_1[0], line_1[1]) + line_2[0];
        line_3[1] = max(max(line_1[0], line_1[1]), line_1[2]) + line_2[1];
        line_3[2] = max(line_1[1], line_1[2]) + line_2[2];

        swap(line_1, line_min);
        line_min[0] = min(line_1[0], line_1[1]) + line_2[0];
        line_min[1] = min(min(line_1[0], line_1[1]), line_1[2]) + line_2[1];
        line_min[2] = min(line_1[1], line_1[2]) + line_2[2];
    }

    cout << *max_element(line_3, line_3 + 3) << " "
         << *min_element(line_min, line_min + 3);
}
