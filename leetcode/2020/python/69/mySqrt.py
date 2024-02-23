class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        l = 1
        r = x + 1
        while l < r:
            m = l + (r-l)//2
            if m*m == x:
                return m
            if m*m > x:
                r = m
            else:
                l = m + 1
        return l-1
