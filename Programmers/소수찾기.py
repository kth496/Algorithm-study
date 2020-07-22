from itertools import permutations
import math


def isPrime(x):
    if x == 1 or x == 0:
        return False
    if x == 2:
        return True
    it = int(math.sqrt(x))+2
    for i in range(2, it):
        if (x % i == 0):
            return False
    return True


def solution(numbers):
    numbers = list(numbers)
    n = len(numbers)
    primeSet = set()
    ans = 0
    for i in range(1, n+1):
        for j in permutations(numbers, i):
            key = int(''.join(j))
            if (isPrime(key) and (key not in primeSet)):
                primeSet.add(key)
                ans += 1
    return ans


s = "011"
print(solution(s))
