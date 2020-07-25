''' #정답은 나오는데 효율성 0인 코드
def isAll(arr):
    for e in arr:
        if (e is 0):
            return False
    return True


def solution(gems):
    # 1
    catego = set(gems)
    gemDic = {}
    i = 0
    for e in catego:
        if (e not in gemDic):
            gemDic[e] = i
            i += 1
    n = len(catego)
    isStol = [0 for i in range(n)]

    # 2
    N = len(gems)
    ret = [0, N]
    for i in range(N-1):
        isStol_ = isStol[:]
        for j in range(i, N):
            isStol_[gemDic[gems[j]]] = 1
            if (isAll(isStol_)):
                if (ret[1]-ret[0]) > (j-i):
                    ret = [i, j]
    return [i+1 for i in ret]
'''

'''
def isAll(arr):
    for e in arr:
        if (e is 0):
            return False
    return True


def solution(gems):
    # 1
    catego = set(gems)
    gemDic = {}
    i = 0
    for e in catego:
        if (e not in gemDic):
            gemDic[e] = i
            i += 1
    n = len(catego)
    isStol = [0 for i in range(n)]

    # 최적화 시도 1
    # 만약 gems의 0번 인덱스에서 q번 인덱스까지 살펴보았을 때 조건이 성립하면,
    # 0 부터 q+1 이상의 모든 인덱스도 조건 성립이다.
    # 따라서 맨 처음 탐색에서 Upper bound를 찾아보자.
    # -> 실패

    # 2
    N = len(gems)
    ret = [0, N]
    for i in range(N-1):
        isStol_ = isStol[:]
        for j in range(i, N):
            isStol_[gemDic[gems[j]]] = 1
            if (isAll(isStol_)):
                if (i == 0):  # 첫 탐색에서 uppper bound 설정
                    N = j
                if (ret[1]-ret[0]) > (j-i):
                    ret = [i, j]
    return [i+1 for i in ret]

'''




import heapq
from collections import defaultdict
def whichBetter(x, y):
    if (x[1] - x[0]) > (y[1] - y[0]):
        return y
    return x


def solution(gems):
    # 1
    gemSet = set(gems)
    gemCnt = len(gemSet)
    gemDic = {}

    # 1 - 2
    N = len(gems)
    l = 0
    r = 0
    ret = [0, N]
    gemDic[gems[0]] = 1

    # 3
    while (1):
        if (l == N):
            break

        if len(gemDic) == gemCnt:
            ret = whichBetter(ret, [l, r])
            lg = gems[l]
            gemDic[lg] -= 1
            if gemDic[lg] == 0:
                gemDic.pop(lg)
            l += 1
        else:
            r += 1
            if (r == N):
                break
            rg = gems[r]
            if rg not in gemDic:
                gemDic[rg] = 1
            else:
                gemDic[rg] += 1
    return [e+1 for e in ret]


d = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
d2 = ["AA", "AB", "AC", "AA", "AC"]
print(solution(d))


# defaultdict를 쓰면 딕셔너리에 존재하는지 체크 필요 X, += 1로 할 수 있음


def another(gems):
    answer = [1, len(gems)]
    gemset = set(gems)
    bag = defaultdict(int)

    s, e = 0, 0
    while e < len(gems):
        if len(bag) < len(gemset):
            bag[gems[e]] += 1
            e += 1
        else:
            if bag[gems[s]] == 1:
                del bag[gems[s]]
            else:
                bag[gems[s]] -= 1
            if answer[1] - answer[0] > e - s - 1:
                answer = [s + 1, e]
            s += 1
    return answer


def another2(gems):
    zero = set(gems)
    jew_map = {i: e for e, i in enumerate(zero)}
    goal = len(jew_map)
    jew = [0 for _ in range(goal)]
    total = len(gems)
    minn = [0, total]  # 시작인덱스, 길이
    s, e = 0, 0
    stat = False
    while s <= e and e < len(gems):
        if total-s < goal or minn[1] == goal:
            break
        if e-s >= minn[1]:
            jew[jew_map[gems[s]]] -= 1
            if jew[jew_map[gems[s]]] == 0:
                zero.add(gems[s])
                stat = False
            s += 1
            continue
        if stat:
            # 최소니?
            if e-s < minn[1]:
                minn = [s, e-s]
            # 먼저 시작하니?
            elif e-s == minn[1] and s < minn[0]:
                minn[0] = s
            jew[jew_map[gems[s]]] -= 1

            if jew[jew_map[gems[s]]] == 0:
                zero.add(gems[s])
                stat = False
            s += 1
        else:
            jew[jew_map[gems[e]]] += 1

            if gems[e] in zero:
                zero.remove(gems[e])
                if len(zero) == 0:
                    stat = True
            e += 1

    return [minn[0]+1, minn[0]+minn[1]]


test = [1, 3, 2, 2, 1, 2, 4, 5, 5, 3, 1, 2, 3, 4, 5]
print(solution(test))
print(another(test))
print(another2(test))


'''
수고많으십니다.

카카오 코딩테스트 보석쇼핑문제(https://programmers.co.kr/learn/courses/30/lessons/67258)를 풀던 중 채점에 의문이 생겨서 문의드립니다. 

풀고나서 다른 사람의 풀이를 보던 중에, 제가 임의로 만들어본 테스트 케이스를 제대로 통과하지 못하는 풀이를 발견했습니다. 그래서 만약 채점용 테스트케이스를 카카오로부터 제공받았다면, 실제 코테에서도 문제가 있었다고 생각합니다. 

문제가 되는 테스트 케이스는 아래와 같습니다.
입력 : [1, 3, 2, 2, 1, 2, 4, 5, 5, 3, 1, 2, 3, 4, 5]
정답 : [11, 15]

통과된 풀이중에서 일부가 위 테스트 케이스에 대해 [5, 10] 등, 이상한 답을 출력함에도 정답으로 처리되어있습니다.

https://programmers.co.kr/learn/courses/30/lessons/67258/solution_groups?language=python3

일단 제가 찾은 것은 위 페이지에서 박효빈, 서지환 님의 풀이가 제대로된 정답을 출력하지 못합니다. 이 외에도, while문에서 오른쪽 보석 위치의 탈출 조건을 제대로 명시하지 못하면 모두 이 케이스에서 걸리게 됩니다.

카카오 인턴십 채용에 사용되었던 문제입니다. 그래서 채점용 테케를 카카오로부터 제공받은것인지 여쭙고 싶습니다. 감사합니다.

김태홍 드림

'''
