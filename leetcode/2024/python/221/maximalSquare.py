class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        cache = {}
        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS:
                return 0
            if (i, j) not in cache:
                down = dfs(i+1, j)
                right = dfs(i, j+1)
                diag = dfs(i+1, j+1)
                cache[(i, j)] = 0
                if matrix[i][j] == '1':
                    cache[(i, j)] = 1 + min(down, right, diag)
            return cache[(i, j)]
        dfs(0, 0)
        return max(cache.values()) ** 2
