from itertools import permutations
import itertools as it
import re
import copy


def cal(x):
    a = int(x[0])
    b = int(x[2])
    if x[1] == '*':
        return a * b
    if x[1] == '+':
        return a + b
    return a - b


def solution(s):
    origin = re.split('(\D)', s)
    parsed = re.split('(\D)', s)
    ret = 0
    operators = ['*', '+', '-']
    prior_cases = [[0, 1, 2], [0, 2, 1], [
        1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    for prior in prior_cases:
        parsed = copy.deepcopy(origin)
        for p in prior:
            # for idx, e in enumerate(parsed):
            idx = 0
            e = parsed[0]
            while (1):
                if (e is operators[p]):
                    prev = parsed[:idx-1]
                    nextt = parsed[idx+2:]
                    val = cal(parsed[idx-1:idx+2])
                    parsed = prev + [val] + nextt
                    idx = 0
                    e = parsed[0]
                else:
                    idx += 1
                    if len(parsed) == 1:
                        ret = max(ret, abs(parsed[0]))
                        break
                    if len(parsed) == idx:
                        break
                    e = parsed[idx]

    return ret


def solution2(expression):
    # 1
    op = [x for x in ['*', '+', '-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)', expression)

    # 2
    a = []
    for x in op:
        _ex = ex[:]  # DeepCopy
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    # 3
    return max(abs(int(x)) for x in a)


d = "100-200*300-500+20"

# solution2(d)

a = [1, 2, 3, 4, 5]

tt = it.permutations(a, 3)
tt = it.combinations(a, 3)
for a in tt:
    print(a)
