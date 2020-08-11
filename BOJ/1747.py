n = int(input())
MAXN = 10000003

era = [1 for _ in range(MAXN)]
era[0] = era[1] = 0


def isPrime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(3, sqrt(x)+1):
        if x % i == 0:
            return False
    return True


def isP(x):
    s = str(x)
    for i in range(len(s) // 2 + 1):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


for i in range(2, MAXN):
    if era[i] == 1:
        if isPrime:
            for j in range(i*2, MAXN, i):
                era[j] = 0
        else:
            era[i] = 0

for x in range(n, MAXN):
    if era[x] == 1 and isP(x):
        print(x)
        break

# for i, r in enumerate(era[:1000]):
#     print(i, r)

'''
#include <iostream>
using namespace std;

int N, p[1003002];

bool isPal(int p) {
	int r = p, q = 0;
	while (r) {
		q *= 10;
		q += r % 10;
		r /= 10;
	}
	return p == q;
}

int main() {
	p[1] = 1;
    /*
     * 에라토스테네스의 체를 더 간단하게 구현하는 C++ 코드
     * 전역변수 영역에 배열 p를 선언하면 원소들은 모두 0으로 초기화된다.
     * for 루프를 순회하면서 만약 0이라면 소수일 가능성이 존재한다는 의미이므로(아직 방문 X 니까)
     * i*i 부터 최대값 전까지 i만큼 증가시켜가면서 0이 아닌 어떤 수로 표시해두면 된다.
     * 나는 i*2 부터 순회하는 것으로 구현했는데 i*i가 조금 더 효율적이다.
     * 어떤 수 i에 대해, i*2 부터 순회할 필요가 없는 이유는, i*2는 이미 i=2일때 살펴보기 때문이다.
     * 같은 논리로 i*3은 이미 3의 배수이므로 i=3일때 이미 살펴보았다.
     * i*2 부터 i*(i-1) 까지는 이미 그 전에 다 체크가 되어있다. 그러므로 i*i부터 순회해도 된다.

     * 문제의 정답을 찾는 while 루프도 잘 살펴보자. 의미상으로 매우 깔끔하고 코드도 간결하다.
     */
	for (int i = 2; i <= 1001; i++) if (!p[i])
		for (int j = i * i; j <= 1003001; j += i) p[j] = i;

	cin >> N;
	while (!(!p[N] && isPal(N))) N++;
	cout << N;
}
'''
