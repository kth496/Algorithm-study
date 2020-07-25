# stones	                        k	result
# [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	3	3

'''
정확성 다 맞고, 효율성 0점
'''


def solution_(stones, k):  # O (N^2)
    answer = 0

    i = 0
    n = len(stones)
    while (True):
        if (i == n):
            answer += 1
            i = 0
            continue
        elif (stones[i] == 0):
            k_ = 0
            for j in range(k+1):
                k_ = j
                if ((i+j) >= n)or(stones[i+j] != 0):
                    break
            if (k_ == k):
                return answer
            else:
                i += k_
                if (i >= n):
                    answer += 1
                    i = 0
                    continue
        stones[i] -= 1
        i += 1


# 이것도 효율성 0점
def solution(stones, k):
    answer = float('inf')
    n = len(stones)
    for i in range(n-k+1):
        # snip = stones[i:i+k]
        # answer = min(answer, max(snip))
        maxx = 0
        for j in range(i, i+k):
            maxx = max(maxx, stones[j])
        answer = min(answer, maxx)
    return answer


'''
import copy
 
INF = 200000000
 
def solution(stones, k):
    left = 1; right = INF
 
    while left <= right:
        mid = (left + right) // 2
        tmp = copy.deepcopy(stones)
        for i in range(len(tmp)):
            tmp[i] -= mid
 
        cnt = 0
        check = False
        for i in range(len(tmp)):
            if tmp[i] <= 0:
                cnt += 1
            else:
                cnt = 0
 
            if cnt >= k:
                check = True
                break
 
        if check is True:
            right = mid - 1
        else:
            left = mid + 1
 
    return left
'''
t1, k1 = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3
print(solution(t1, k1))
