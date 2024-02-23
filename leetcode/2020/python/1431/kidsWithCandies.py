class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        m = max(candies)
        res = []
        for i in candies:
            if i + extraCandies >= m:
                res.append(True)
            else:
                res.append(False)
        return res
