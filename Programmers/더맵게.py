import heapq


def solution(scv, K):
    answer = 0
    heapq.heapify(scv)

    while scv:
        # 조건 만족시 종료
        if scv[0] >= K: return answer

        if len(scv) == 1: return -1

        # 새 음식 만들기
        answer += 1
        # newf = scv[0] + scv[1] * 2
        # heapq.heappop(scv)
        # heapq.heappop(scv)
        heapq.heappush(scv, heapq.heappop(scv) + heapq.heappop(scv) * 2)


print(solution([0, 0], 4))
