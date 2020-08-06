T = int(input())

for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    minA = min(a)
    minB = min(b)

    cnt = 0
    for i in range(N):
        if (a[i] > minA) and (b[i] > minB):
            which = min(abs(a[i]-minA), abs(b[i]-minB))
            cnt += which
            a[i] -= which
            b[i] -= which
            cnt += (a[i] - minA + b[i] - minB)
            continue
        if (a[i] > minA):
            cnt += (a[i] - minA)
            continue
        if (b[i] > minB):
            cnt += (b[i] - minB)
            continue
    print(cnt)

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
        std::vector<int> a(n), b(n);
        for (int i = 0; i < n; ++i)
            std::cin >> a[i];
        for (int i = 0; i < n; ++i)
            std::cin >> b[i];
        int na = *std::min_element(a.begin(), a.end()); // 이터레이터에 *을 붙이면 값으로 가져온다?
        int nb = *std::min_element(b.begin(), b.end());
        int64_t ans = 0;
        for (int i = 0; i < n; ++i)
            ans += std::max(a[i] - na, b[i] - nb);
        std::cout << ans << "\n";
    }
    return 0;
}
'''
