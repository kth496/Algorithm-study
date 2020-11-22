from typing import List


class Solution:
    visited = []
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    R = 0
    C = 0

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.R = len(board)
        self.C = len(board[0])
        self.visited = [[False for _ in range(self.C)] for _ in range(self.R)]
        for r in range(self.R):
            for c in range(self.C):
                if self.find(board, r, c, board[r][c], word): return True
        return False

    def find(self, board: List[List[str]], r: int, c: int, cur: str, word: str):
        if cur != word[:len(cur)]: return False
        if cur == word: return True

        ret = False
        self.visited[r][c] = True
        for i in range(4):
            nr, nc = r + self.dr[i], c + self.dc[i]
            if 0 <= nr < self.R and 0 <= nc < self.C and not self.visited[nr][nc]:
                ret = ret or self.find(board, nr, nc, cur + board[nr][nc], word)
        self.visited[r][c] = False
        return ret
