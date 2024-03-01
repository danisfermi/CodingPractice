class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [0] * (n+1)
        for i in range(m-1, -1, -1):
            nextdp = dp.copy()
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    nextdp[j] = 1 + dp[j+1]
                else:
                    nextdp[j] = max(nextdp[j+1], dp[j])
            dp = nextdp
        return dp[0]
        '''
        cache = {}
        def lcs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            res = 0
            if text1[i] == text2[j]:
                res = 1+lcs(i+1, j+1)
            else:
                res = max(lcs(i+1, j), lcs(i, j+1))
            cache[(i,j)] = res
            return res
        return lcs(0, 0)
        '''
