import sys
input = sys.stdin.readline

T = int(input())
ans = []
for tc in range(T):
    # N은 스택 수, K는 각 스택의 접시 수, P는 최대 선택 가능 접시 수
    N, K, P = map(int, input().split())

    # dp[N][P]
    dp = [[0 for _ in range(P+1)] for _ in range(N+1)]
    stack = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N+1):
        for j in range(1, P+1):
            for x in range(min(j+1, K+1)):
                dp[i][j] = max(sum(stack[i-1][:x])+dp[i-1][j-x], dp[i][j])

    # print("Case #%d: %d" % (tc+1, dp[N][P]))
    ans.append("Case #%d: %d" % (tc+1, dp[N][P]))
for e in ans:
    print(e)


'''
그리디는 절대 아니다.
예제 1을 살펴보면 P=5일때는 위에서 3개, 아래에서 2개를 고르지만,
P=4일때는, 아래에서 4개를 고르는게 답이다. 따라서 dp계열 문제라는 느낌이 온다.

'''

'''
Python

rstrip을 하라는 건 문자열 자체를 변수에 저장하고 싶을 때 얘기지, 
개행문자가 맨 끝에 들어와도 int 변환이나 split()을 그대로 할 수 있습니다. 
즉 int(sys.stdin.readline()), sys.stdin.readline().split() 이렇게 해도 아무 문제 없습니다.
참고로 이름이 꽤 길기 때문에 저는 input = sys.stdin.readline을 맨 처음에 함으로써 쓰는 편입니다.
'''

'''
위 방법대로 입출력을 해봐도 TLE나와서 cpp로 다시풀었음.
'''
