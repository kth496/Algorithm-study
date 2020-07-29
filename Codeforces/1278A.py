'''
The length of p does not exceed 100

hash와 p(p')의 길이가 최대 100이라고 주어졌기 때문에 O(N^2)으로 충분히 해결 가능하다.
'''


from collections import defaultdict


def isSame(dic1, dic2):
    for k in dic1.keys():
        if k not in dic2:
            return False
        else:
            if (dic1[k] != dic2[k]):
                return False
    return True


def makeDic(s):
    ret = defaultdict(int)
    for c in s:
        ret[c] += 1
    return ret


T = int(input())
for _ in range(T):
    p = input()
    h = input()

    if len(p) > len(h):
        print("NO")
        continue

    pDic = makeDic(p)

    lim = len(h) - len(p)
    itv = len(p)
    isYes = False
    for i in range(lim + 1):
        dic = defaultdict(int)
        snip = h[i:i+itv]
        hDic = makeDic(snip)
        if (isSame(pDic, hDic)):
            print("YES")
            isYes = True
            break
    if not isYes:
        print("NO")
