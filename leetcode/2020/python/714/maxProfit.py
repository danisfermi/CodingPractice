class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        buyStock = -prices[0]
        noStock = 0
        for i in xrange(1, n):
            preBuyStock = buyStock
            preNoStock = noStock
            buyStock = max(preNoStock - prices[i], preBuyStock)
            noStock = max(preBuyStock + prices[i] - fee, preNoStock)
        return noStock
