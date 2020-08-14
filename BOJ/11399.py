'''
5
3 1 4 3 2
'''
N = int(input())
person = list(map(int, input().split()))

# person = 1 2 3 3 4
# wait   = 1 3 6 9 13
# sumofwait = 32

person = sorted(person)
wait = [0]
for i in range(N):
    wait.append(wait[i] + person[i])
# print(person)
# print(wait)
print(sum(wait))
