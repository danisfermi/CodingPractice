class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def feasible(days):
            bo = 0
            flo = 0
            for bloom in bloomDay:
                if bloom > days:
                    flo = 0
                else:
                    bo += (flo + 1) // k
                    flo = (flo + 1) % k
            return bo >= m           
        if len(bloomDay) < m*k:
            return -1
        l = 1
        r = max(bloomDay)
        while l < r:
            mid = l + (r-l)//2
            if feasible(mid):
                r = mid
            else:
                l = mid+1
        return l
