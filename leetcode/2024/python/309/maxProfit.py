class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def helper(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in cache:
                return cache[(i, buying)]
            if buying:
                res1 = helper(i+1, not buying) - prices[i] 
                res2 = helper(i+1, buying)
            else:
                res1 = helper(i+2, not buying) + prices[i]
                res2 = helper(i+1, buying)
            res = max(res1, res2)
            cache[(i, buying)] = res
            return res
        return helper(0, True)
