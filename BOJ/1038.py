from itertools import combinations

'''
어떤 숫자의 조합이 주어지면, 감소하는 수는 단 하나만 만들 수 있다.
예를 들어, 1,2,5,8 로는 8521만 만들 수 있다.
이 논리를 적용해보면 최대 1023개만 나온다.
'''
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

ret = []

for i in range(1, 11):
    for cand in combinations(a, i):
        tmp = sorted(list(cand), reverse=True)
        s = ''.join(tmp)
        ret.append(int(s))

ret.sort()
n = int(input())
if n >= len(ret):
    print(-1)
else:
    print(ret[n])

'''
#include<iostream>
#include<queue>
using namespace std;

int main(){
	queue<long long> q;
	int n;
	cin >> n;
	if(n>1022) {printf("-1"); return 0;}
	for(int i =0; i<10; ++i) q.push(i);
	while(q.size() && n){
		for(int i =0; i<10; ++i)
			if(q.front() % 10 > i) q.push(q.front()*10 + i);
		q.pop();
		n--;
	}
	cout << q.front();
}
'''
