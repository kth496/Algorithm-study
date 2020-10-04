from itertools import combinations


def boj_printing(iterable):
    for e in iterable:
        print(e, end=" ")
    print()


while True:
    i = input()
    if i == "0":
        exit(0)
    arr = list(map(int, i.split()))
    k = arr[0]
    numbers = arr[1:]
    for case in combinations(numbers, 6):
        boj_printing(case)
    print()
