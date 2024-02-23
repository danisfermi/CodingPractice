class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        for i in xrange(n):
            c = a + b
            a = b
            b = c
        return b
