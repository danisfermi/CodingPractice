class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [1 if not obstacleGrid[0][0] else 0]
        for j in range(1, len(obstacleGrid[0])):
            dp.append(dp[j - 1] if not obstacleGrid[0][j] else 0)
        for i in range(1, len(obstacleGrid)):
            dp[0] = dp[0] if not obstacleGrid[i][0] else 0
            for j in range(1, len(obstacleGrid[i])):
                dp[j] = dp[j] + dp[j - 1] if not obstacleGrid[i][j] else 0
        return dp[-1]
