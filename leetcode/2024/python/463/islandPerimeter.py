class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        self.res = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 1
            if grid[r][c] == 0:
                return 1
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            perim = dfs(r+1, c)
            perim += dfs(r-1, c)
            perim += dfs(r, c+1)     
            perim += dfs(r, c-1) 
            return perim

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return dfs(i, j)
