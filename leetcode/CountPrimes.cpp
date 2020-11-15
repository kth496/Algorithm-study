class Solution {
public:
    int countPrimes(int n) {
        vector<int> chk(n + 1, 0);
        int ans = 0;
        for (int i = 2; i <= n; i++) {
            if (chk[i]) continue;
            for (int j = i * 2; j <= n; j+=i) {
                chk[j] = 1;
            }
        }

        for (int i = 2; i < n; i++) {
            if (!chk[i]) ans++;
        }

        return ans;
    }
};
