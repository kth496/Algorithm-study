import heapq
from collections import deque


def solution(priorities, location):
    q = deque([(id, cur_p) for id, cur_p in enumerate(priorities)])
    pq = list(map(lambda x: -x, priorities))
    heapq.heapify(pq)

    cnt = 0

    while True:
        id, cur_p = q.popleft()

        if pq[0] == cur_p:
            cnt += 1
            heapq.heappop(pq)
            if id == location:
                return cnt
        else:
            q.append((id, -cur_p))
