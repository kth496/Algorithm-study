T = int(input())
tmp = []

for _ in range(T):
    N = int(input())
    w = list(map(int, input().split()))

    d = [0 for _ in range(52)]
    for person in w:
        d[person] += 1

    ans = 0
    for s in range(2*min(w), 2*max(w) + 1):
        cnt = 0
        for wi in set(w):
            if (wi >= s) or (s-wi > max(w)):
                continue
            if (wi * 2) == s:
                cnt += d[wi]
            else:
                cnt += min(d[wi], d[s-wi])
        cnt = cnt // 2
        ans = max(ans, cnt)
    # tmp.append(ans)
    print(ans)

# print(tmp)

'''
// 고수의 풀이 jiangly
#include <bits/stdc++.h>
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t;
    std::cin >> t;
    while (t--) {
        int n;
        std::cin >> n;
        std::vector<int> cnt(n);
        for (int i = 0; i < n; ++i) {
            int w;
            std::cin >> w;
            ++cnt[--w];
        }
        int ans = 0;
        for (int v = 0; v <= 2 * n - 2; ++v) {
            int res = 0;
            for (int i = 0; 2 * i <= v; ++i) {
                if (v - i >= n)
                    continue;
                if (2 * i == v) {
                    res += cnt[i] / 2;
                } else {
                    res += std::min(cnt[i], cnt[v - i]);
                }
            }
            ans = std::max(ans, res);
        }
        std::cout << ans << "\n";
    }
    return 0;
}
'''
