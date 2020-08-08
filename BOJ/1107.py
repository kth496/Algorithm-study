from itertools import product


def sol1():
    N = int(input())
    M = int(input())

    # btn이 1이면 사용가능, 0이면 불가
    btn = set([i for i in range(10)])
    if M != 0:
        for i in list(map(int, input().split())):
            btn.remove(i)

    # print(btn)

    ans = float('inf')

    maxx = len(str(N))
    for i in range(1, maxx+2):
        for e in product(btn, repeat=i):
            # btn 에서는 set으로 관리해야해서 int형이어야 함
            # 따라서 join을 하려면 각 원소를 str형으로 바꿔줘야 함
            cur = int(''.join(map(str, e)))
            ans = min(ans, abs(cur-N) + len(str(cur)))
            # print(cur)

    ans = min(ans, abs(N - 100))
    print(ans)


''' djm의 풀이 '''


def sol2():
    p = input
    n = int(p())
    b = p()if p() > '0'else[]
    print(min([1e9if any(x in str(i)for x in b)else len(str(i))+abs(i-n)
               for i in range(6**8)]+[abs(n-100)]))


''' syphon의 풀이 '''


def sol3():
    n = int(input())
    m = int(input())
    buttons = list(range(10))
    if m:
        for broken in map(int, input().split()):
            buttons.remove(broken)

    dst = abs(n - 100)
    for i in range(max(n * 2, 100)):
        if all([int(x) in buttons for x in str(i)]):
            # i의 각 자리 숫자가 buttons에 있는지를 확인해서(클릭 가능 한지)
            # 있으면 true가 들어가고, 없으면 false가 들어가는 list comprehention
            # 이 리스트를 all함수에 넣어서 확인하는것
            # 정확히는 all함수는 iterable의 각 element를 bool()함수에 넣어서
            # 전부 True가 나오는지 확인한다.
            d = abs(n - i) + len(str(i))
            if d < dst:
                dst = d
    print(dst)


if __name__ == "__main__":
    sol3()
