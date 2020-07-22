from itertools import permutations


def solution(baseball):
    answer = 0
    nums = list(range(1, 10))
    for i in permutations(nums, 3):
        isPos = True
        i = list(map(str, i))
        for row in baseball:
            inp, s, b = row
            s_, b_ = 0, 0
            inp = list(str(inp))
            s1, s2 = set(i), set(inp)
            if (len(s1) < 3):
                isPos = False
                break
            b_ += len(s1 & s2)
            for j in range(3):
                if (i[j] == inp[j]):
                    s_ += 1
            b_ -= s_
            if (s != s_) or (b != b_):
                isPos = False
                break
        if (isPos):
            answer += 1
    return answer


d = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(d))
