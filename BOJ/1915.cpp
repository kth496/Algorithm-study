#include <stdio.h>

int a[1001][1001] = {0};

int min(int a, int b, int c) {
    return (a < b ? a : b) < c ? (a < b ? a : b) : c;
}

int max(int a, int b) { return a > b ? a : b; }

int main() {
    int n, m, i, j, c = 0;
    scanf("%d%d", &n, &m);
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) scanf("%1d", &a[i][j]);
    }
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) {
            if (a[i][j] != 0) {
                a[i][j] = min(a[i - 1][j - 1], a[i - 1][j], a[i][j - 1]) + 1;
                c = max(c, a[i][j]);
            }
        }
    }
    printf("%d", c * c);
}