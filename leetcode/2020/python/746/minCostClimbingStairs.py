class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        f = [0] * n
        f[0] = cost[0]
        f[1] = cost[1]
        for i in xrange(2, n):
            f[i] = cost[i] + min(f[i-1], f[i-2])
        return min(f[n-1], f[n-2])
