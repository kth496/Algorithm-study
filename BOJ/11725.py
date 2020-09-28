from collections import deque

N = int(input())
data = [-1 for _ in range(N + 1)]
adj = [[] for _ in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

data[1] = 0

q = deque()
q.append(1)
while len(q) > 0:
    par = q.popleft()
    for child in adj[par]:
        if data[child] == -1:
            data[child] = par
            q.append(child)

for i in range(2, N + 1):
    print(data[i])
