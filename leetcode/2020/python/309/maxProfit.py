class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 0:
            return 0
        buyStock = -prices[0] 
        sellStock = -float('inf')
        noStock = 0
        for i in xrange(1,n):
            preBuyStock = buyStock
            preSellStock = sellStock
            preNoStock = noStock
            buyStock = max(preNoStock - prices[i], preBuyStock)
            sellStock = preBuyStock + prices[i]
            noStock = max(preNoStock, preSellStock)
        return max(sellStock, noStock)
