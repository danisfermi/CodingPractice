class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        cache = {}
        def helper(i, j, prev):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return 0
            if matrix[i][j] <= prev:
                return 0
            if (i, j, prev) in cache:
                return cache[(i, j, prev)]
            res = 1
            res = max(res, 1 + helper(i, j+1, matrix[i][j]))
            res = max(res, 1 + helper(i+1, j, matrix[i][j]))
            res = max(res, 1 + helper(i, j-1, matrix[i][j]))
            res = max(res, 1 + helper(i-1, j, matrix[i][j]))
            cache[(i, j, prev)] = res
            return res
            
        for i in range(ROWS):
            for j in range(COLS):
                helper(i, j, -1)
                
        return max(cache.values())
                
        
            
