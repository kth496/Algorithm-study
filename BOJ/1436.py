N = int(input())

n = 0
i = 666
while (True):
    s = str(i)
    if s.find("666") != -1:
        n += 1
    if n == N:
        print(i)
        exit()
    i += 1
