def rotate(matrix):
    N = len(matrix)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N - 1 - r] = matrix[r][c]
    return ret


def is_lock_opened(cur_state, n, m):
    for r in range(m - 1, m - 1 + n):
        for c in range(m - 1, m - 1 + n):
            if cur_state[r][c] != 1:
                return False
    return True


def solution(key, lock):
    N = len(lock)
    M = len(key)

    # 자물쇠 크기 확장
    lock_board = [[0 for _ in range(N + 2 * M - 2)] for _ in range(N + 2 * M - 2)]
    for y in range(N):
        for x in range(N):
            lock_board[y + M - 1][x + M - 1] = lock[y][x]
    lock = lock_board

    if is_lock_opened(lock, N, M):
        return True

    def combine(r_, c_, type_):
        for y in range(M):
            for x in range(M):
                lock[y + r_][x + c_] += (key[y][x] * type_)

    for r in range((N + M - 1)):
        for c in range((N + M - 1)):
            for _ in range(4):
                # 끼워맞춰보기
                combine(r, c, 1)
                if is_lock_opened(lock, N, M):
                    return True
                # 해제하기
                combine(r, c, -1)
                # 회전
                key = rotate(key)
    return False
