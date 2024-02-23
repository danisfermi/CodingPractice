class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        curr = [1 for i in xrange(n)]
        for i in xrange(1,m):
            for j in xrange(1,n):
                curr[j] += curr[j-1]
        return curr[n-1]
