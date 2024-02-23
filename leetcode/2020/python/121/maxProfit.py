class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for i in xrange(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif maxProfit < prices[i] - minPrice:
                maxProfit = prices[i] - minPrice
        return maxProfit
