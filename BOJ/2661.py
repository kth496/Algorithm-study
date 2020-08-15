N = int(input())

cand = ['1', '2', '3']


def isGood(numList):
    # 여기에서 인접 부분수열 비교연산 걸리면 false
    n = len(numList)//2
    for i in range(1, n+1):  # i는 비교할 부분수열의 길이를 의미함
        for l in range(len(numList)-i):
            left = numList[l:l+i]
            right = numList[l+i:l+2*i]
            if left == right:
                return False
    return True


ans = []


def dfs(a):
    global ans
    if a == N+1:
        print(''.join(ans))
        exit()
    for _ in range(a, N+1):
        for num in cand:
            if isGood(ans+[num]):
                ans = ans + [num]
                dfs(a+1)
                ans.pop()


dfs(1)
