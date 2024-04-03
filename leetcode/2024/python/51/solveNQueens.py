class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        col = set()
        posDia = set()
        negDia = set()
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c in col or (r-c) in posDia or (r+c) in negDia:
                    continue
                col.add(c)
                posDia.add(r-c)
                negDia.add(r+c)
                board[r][c] = "Q"
                backtrack(r+1)
                col.remove(c)
                posDia.remove(r-c)
                negDia.remove(r+c)
                board[r][c] = "."
        backtrack(0)
        return res
