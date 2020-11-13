from typing import List
from collections import deque


def solution(skill: str, skill_trees: List[str]) -> int:
    answer = 0
    for case in skill_trees:
        q = deque(list(skill))
        q2 = deque(list(case))

        while True:
            # 스킬을 다 배웠으면 종료
            if not q2:
                answer += 1
                break

            # 스킬 습득 순서와 일치하면 큐에서 뽑음
            if q and q[0] == q2[0]:
                q.popleft()
                q2.popleft()
                continue

            # 스킬 습득 순서를 위반하는 스킬이 존재하면 종료
            if q and any([q2[0] == c for c in q]):
                break

            # 스킬을 배움( = 큐에서 뽑음)
            q2.popleft()

    return answer
