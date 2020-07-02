"""
3
2 1
0 1
4 6
0 1 1 2 2 3 3 0 0 2 1 3
6 10
0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5
"""
studentNumber = 0
friendCase = 0
areFriends = [[0 for _ in range(10)]
              for _ in range(10)]


def recur(hasFriend):
    fronStudent = -1
    for i in range(studentNumber):
        if hasFriend[i] == 0:
            fronStudent = i
            break

    if fronStudent == -1:
        return 1

    ret = 0
    for pair in range(fronStudent+1, studentNumber):
        if(hasFriend[pair] == 0 and areFriends[fronStudent][pair]):
            hasFriend[pair] = hasFriend[fronStudent] = 1
            ret += recur(hasFriend)
            hasFriend[pair] = hasFriend[fronStudent] = 0
    return ret


tc = int(input())
for _ in range(tc):
    studentNumber, friendCase = map(int, input().split())
    hasFriend = [0 for _ in range(studentNumber)]
    for a in range(studentNumber):
        for b in range(studentNumber):
            areFriends[a][b] = 0
    data = list(map(int, input().split()))

    for e in range(friendCase):
        i, j = data[e*2], data[e*2+1]
        areFriends[i][j] = 1
        areFriends[j][i] = 1
    print(recur(hasFriend))
