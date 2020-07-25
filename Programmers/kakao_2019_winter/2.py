from collections import Counter
import re


def solution2(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))


def solution(s):
    s = s[1:-1]
    sett = re.findall('\{(.*?)\}', s)
    sett.sort(key=len)

    ret = []
    dupdic = {}
    for each_set in sett:
        es = list(map(int, each_set.split(',')))
        for e in es:
            if (e not in dupdic):
                ret.append(e)
                dupdic[e] = 1
                continue
    return ret


# 1588 5580
t = "{{4, 2, 3}, {3}, {2, 3, 4, 1}, {2, 3}}"

print(solution(t))
