class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0
        for i in xrange(0, n):
            buy1 = min(buy1, prices[i])
            sell1 = max(sell1, prices[i] - buy1)
            buy2 = min(buy2, prices[i]-sell1)
            sell2 = max(sell2, prices[i] - buy2)
        return sell2
