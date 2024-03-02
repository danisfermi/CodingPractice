class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for i in range(len(coins)-1, -1, -1):
            nextdp = dp.copy()
            for j in range(1, amount+1):
                if j - coins[i] >= 0:
                    nextdp[j] += nextdp[j-coins[i]]
            dp = nextdp
        return dp[amount]
        '''
        cache = {}
        def helper(i, total):
            if total == amount:
                return 1  
            if total > amount:
                return 0 
            if i >= len(coins):
                return 0
            if (i,total) in cache:
                return cache[(i, total)]
            res = helper(i+1, total) + helper(i, total+coins[i])
            cache[(i, total)] = res
            return res
        return helper(0, 0)
        '''
