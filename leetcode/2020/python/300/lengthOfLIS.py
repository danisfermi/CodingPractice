class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def bsUtil(sub, i):
            l = 0
            r = len(sub)-1
            while l <= r:
                m = l + (r-l)//2
                if sub[m] < i:
                    l = m + 1
                elif sub[m] > i:
                    r = m - 1
                else:
                    return m
            return l
        sub = []
        for i in nums:
            pos = bsUtil(sub, i)
            if len(sub) == pos:
                sub.append(i)
            else:
                sub[pos] = i
        return len(sub)
