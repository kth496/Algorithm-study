N = int(input())
if N == 2:
    print(1)
    exit()
adj = [[0 for _ in range(N)] for _ in range(N)]

start = 0
par = list(map(int, input().split()))

# i : child
# e : parent
for i, e in enumerate(par):
    if e == -1:
        start = i
    else:
        adj[i][e] = 1
        adj[e][i] = -1

delNode = int(input())

countOfChild = 0
childPos = 0
for i in range(N):
    if adj[start][i] == -1:
        countOfChild += 1
        childPos = i

if countOfChild == 1 and delNode == start:
    start = childPos

for i in range(N):
    if adj[delNode][i] == 1 or adj[delNode][i] == -1:
        adj[i][delNode] = 0
    adj[delNode][i] = 0

# for row in adj:
#     print(row)


def dfs(a):
    countOfOne = 0
    isStem = False
    ret = 0
    for next_, val in enumerate(adj[a]):
        if val == 1:
            countOfOne += 1
        if val == -1:
            isStem = True
            ret += dfs(next_)
    if countOfOne == 1 and not isStem:
        return 1
    return ret


print(dfs(start))


'''
if 문으로 더러워진 부분은 
3
-1 0 1
0
과 같은 케이스를 처리하기 위해서이다. 이런 경우 트리의 모양은 아래와 같다.


          0
            \
             \
              1
               \
                \
                 2

따라서 0번 노드를 지워버리면 1번 노드가 루트노드가 되면서 2번노드가 여전히 리프노드가 된다.
if문을 안쓰고 해결할수도 있을 것 같은데, 그 부분은 최적화를 고민해봐야겠다.

'''
