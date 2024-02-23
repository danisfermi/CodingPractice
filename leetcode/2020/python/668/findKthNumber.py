class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def enough(num):
            count = 0
            for val in range(1, m + 1):
                add = min(num // val, n)
                if add == 0:
                    break
                count += add
            return count >= k                

        left, right = 1, n * m
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left
