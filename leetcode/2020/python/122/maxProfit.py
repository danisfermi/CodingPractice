class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        res = 0
        for i in xrange(1,len(prices)):
            if prices[i] > prices[i-1]:
                res += (prices[i] - prices[i-1])
        return res
