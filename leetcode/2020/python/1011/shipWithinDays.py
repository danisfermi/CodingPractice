class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def canShip(weight):
            days = 1
            total = 0
            for i in weights:
                total += i
                if total > weight:
                    total = i
                    days += 1
                    if days > D:
                        return False
            return True
        l = max(weights)
        r = sum(weights)
        while l < r:
            m = l + (r-l)//2
            if canShip(m):
                r = m
            else:
                l = m + 1
        return l
