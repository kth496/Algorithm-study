N = int(input())
data = []
for _ in range(N):
    data.append(input())
data = list(set(data))
data = sorted(data, key = lambda x : (len(x), x))
for e in data:
    print(e)