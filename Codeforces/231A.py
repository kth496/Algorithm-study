n = int(input())
cnt = 0
for _ in range(n):
    s = list(map(int, input().split()))
    if (s.count(1) >= 2):
        cnt += 1
print(cnt)
