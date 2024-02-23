class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def feasible(m):
            return sum(((pile-1)/m + 1) for pile in piles) <= H
        l = 1
        r = max(piles)
        while l < r:
            m = l + (r-l)//2
            if feasible(m):
                r = m
            else:
                l = m+1
        return l
