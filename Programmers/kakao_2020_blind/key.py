def rotate(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret


def cover(_r, _c, key, exLock, op):
    for r in range(_r, _r+3):
        for c in range(_c, _c+3):
            if op == 1:
                exLock[r][c] += key[r-_r][c-_c]
            else:
                exLock[r][c] -= key[r-_r][c-_c]
    return exLock


def isMatch(_r, _c, key, exLock):
    for _ in range(4):  # rotaion
        isPossible = True
        # cover
        exLock = cover(_r, _c, key, exLock, 1)

        # check
        for y in range(2, 5):
            for x in range(2, 5):
                if (exLock[y][x] is not 1):
                    isPossible = False
        if isPossible:
            return True

        # uncover
        exLock = cover(_r, _c, key, exLock, -1)
        key = rotate(key)
    return False


def solution(key, lock):
    # Re-init
    exLock = [[-1 for i in range(4+len(lock[0]))] for i in range(4+len(lock))]
    for r in range(2, 2 + len(lock)):
        for c in range(2, 2 + len(lock[0])):
            exLock[r][c] = lock[r-2][c-2]

    # solve
    for r in range(0, 5):
        for c in range(0, 5):
            if isMatch(r, c, key, exLock):
                return True
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# key = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# lock = [[0, 1, 1], [0, 0, 0], [1, 1, 1]]

print(solution(key, lock))
