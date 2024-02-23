class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < k or k == 0:
            return 0
        buy = [float('inf')] * k
        sell = [0] * k
        for i in xrange(n):
            for j in xrange(0,k):
                if j == 0:
                    buy[j] = min(buy[j], prices[i])
                else:
                    buy[j] = min(buy[j], prices[i] - sell[j-1])
                sell[j] = max(sell[j], prices[i] - buy[j])
        return sell[k-1]
