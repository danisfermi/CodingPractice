class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1 : 1}
        for num in range(2, n+1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                dp[num] = max(dp[num], dp[i] * dp[num-i])
        return dp[n]
        '''
        cache = {}
        def dfs(num):
            if num == 1:
                return 1
            if num in cache:
                return cache[num]
            cache[num] = 0 if num == n else num
            for i in range(1, num):
                cache[num] = max(cache[num], dfs(i) * dfs(num-i))
            return cache[num]
        return dfs(n)
        '''
