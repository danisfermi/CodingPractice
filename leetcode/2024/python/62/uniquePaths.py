class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr_row = [1] * n
        prev_row = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                curr_row[j] = curr_row[j - 1] + prev_row[j]    
            curr_row, prev_row = prev_row, curr_row
        
        return prev_row[-1]
