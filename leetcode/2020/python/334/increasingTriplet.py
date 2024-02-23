class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def bsUtil(sub, i):
            l = 0
            r = len(sub)-1
            while l <= r:
                m = l + (r-l) // 2
                if sub[m] == i:
                    return m
                elif sub[m] > i:
                    r = m - 1
                else:
                    l = m + 1
            return l
        sub = []
        for i in nums:
            pos = bsUtil(sub, i)
            if pos == len(sub):
                sub.append(i)
            else:
                sub[pos] = i
            if len(sub) >= 3:
                return True
        return False
