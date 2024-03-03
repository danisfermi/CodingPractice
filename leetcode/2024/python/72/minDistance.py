class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float('inf') for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1) - i
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]
        '''
        memo = {}
        def dfs(i, j):
            if i == 0 or j == 0: return j or i         
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i-1] == word2[j-1]:
                ans = dfs(i-1, j-1)
            else: 
                ans = 1 + min(dfs(i, j-1), dfs(i-1, j), dfs(i-1, j-1))
            memo[(i,j)] = ans
            return memo[(i,j)]
        
        return dfs(len(word1), len(word2))
        '''
