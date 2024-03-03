class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False
        dp = [[False for _ in range(l2+1)] for _ in range(l1+1)]
        dp[l1][l2] = True
        for i in range(l1, -1, -1):
            for j in range(l2, -1, -1):
                if i < l1 and s3[i+j] == s1[i] and dp[i+1][j]:
                    dp[i][j] = True
                if j < l2 and s3[i+j] == s2[j] and dp[i][j+1]:
                    dp[i][j] = True
        return dp[0][0]
        '''
        cache = {}
        def helper(i1, i2):
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            if i1 == len(s1) and i2 == len(s2):
                return True
            res = False
            if i1 < len(s1) and s3[i1+i2] == s1[i1] and helper(i1+1, i2):
                res = True
            if i2 < len(s2) and s3[i1+i2] == s2[i2] and helper(i1, i2+1):
                res = True
            cache[(i1, i2)] = res
            return res
        return helper(0, 0)
        '''     
