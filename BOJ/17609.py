T = int(input())


def isPal(s, turn):
    n = len(s)
    key = (n - 1)//2
    isPos = 0
    for i in range(key+1):
        if (s[i] != s[n-1-i]):
            if turn:
                return 2
            ret1 = isPal(s[:i] + s[i+1:], True)
            ret2 = isPal(s[:n-1-i] + s[n-i:], True)
            isPos = min(ret1, ret2) + 1
            break
    return isPos-1 if isPos == 3 else isPos


for _ in range(T):
    d = input()
    print(isPal(d, False))

''' 블루꺼 풀이
#include<bits/stdc++.h>
using namespace std;
int T,len,ans1=0,ans2=0,cnt; string s;
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin>>T;
	while(T--){
		cin>>s;
		len=s.length(); ans1=ans2=0;
		for(int i=0,j=len-1; i<=j; i++,j--) if(s[i]!=s[j]) ans1++,j++;
		for(int i=0,j=len-1; i<=j; i++,j--) if(s[i]!=s[j]) ans2++,i--;
		cout<<min(2,min(ans1,ans2))<<'\n';
	}
}
'''
