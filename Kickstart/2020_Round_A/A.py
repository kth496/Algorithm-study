# T = int(input())


# for tc in range(T):
#     N, B = int(input())
#     houses = [0] + list(map(int, input().split()))
#     dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

#     # dp[i][j] = k : i번째 집까지, j개를 택했을 때 비용은 k임
#     dp[1][1] = houses[1]
#     dp[1][0] = 0

#     for i in range(2, N+1):
#         dp[i]


'''
그냥 단순 그리디이다.
'''

T = int(input())


for tc in range(T):
    N, B = map(int, input().split())
    houses = list(map(int, input().split()))
    houses.sort()

    ans = 0
    cost = 0
    for i in houses:
        if (cost + i) <= B:
            cost += i
            ans += 1
        else:
            break
    print("Case #%d: %d" % (tc+1, ans))
