class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)
        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS-1)
        for i in range(COLS):
            dfs(0, i)
            dfs(ROWS-1, i)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "T":
                    board[i][j] = "O"
