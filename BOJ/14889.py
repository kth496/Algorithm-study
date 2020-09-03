from itertools import combinations

n = int(input())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))

person = [i for i in range(n)]

teamList = list(combinations(person, int(n/2)))


ans = float('inf')
for i in range(len(teamList)):
    A = teamList[i]
    B = teamList[len(teamList)-i-1]

    statA = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            x = A[i]
            y = A[j]
            statA += (d[x][y] + d[y][x])

    statB = 0
    for i in range(len(B)):
        for j in range(i, len(B)):
            x = B[i]
            y = B[j]
            statB += (d[x][y] + d[y][x])

    ans = min(ans, abs(statA - statB))

print(ans)

'''
// topology의 c++ 풀이
#include <bits/stdc++.h>
#include <unistd.h>
#ifdef TOPOLOGY
#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
#define debug(...)
#endif
using namespace std;

int main() {
	int n, a[22][22];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &a[i][j]);
		}
	}
	vector<int> perm;
	for (int i = 0; i < n / 2; i++) {
		perm.push_back(0);
	}
	for (int i = 0; i < n / 2; i++) {
		perm.push_back(1);
	}
	int m = (int)1e9;
	do {
		vector<int> v, w;
		for (int i = 0; i < n; i++) {
			if (perm[i]) v.push_back(i);
			else w.push_back(i);
		}
		int dif = 0;
		for (int i = 0; i < n / 2; i++) {
			for (int j = 0; j < n / 2; j++) {
				dif += a[v[i]][v[j]] - a[w[i]][w[j]];
			}
		}
		m = min(m, abs(dif));
	} while (next_permutation(perm.begin(), perm.end()));
	cout << m << endl;
	return 0;
}
/*
문제에서 사람수가 전부 짝수이고, 그래서 절반으로 정확히 나눠진다고 함
그래서 vector<int> perm 에 0과 1을 각각 n/2개씩 집어넣고 비트마스킹처럼 사용가능
이렇게하면 combination이 없더라도, permutation으로 해결 가능하다.
*/

'''
