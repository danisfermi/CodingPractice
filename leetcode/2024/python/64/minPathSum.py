class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 and j == 0:
                    continue
                a = grid[i-1][j] if (i-1) >= 0 and j >= 0 else float('inf')
                b = grid[i][j-1] if (i) >= 0 and (j-1) >= 0 else float('inf')
                grid[i][j] += min(a,b)
        return grid[-1][-1]
