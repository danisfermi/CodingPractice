class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        def enough(distance):
            count, i, j = 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                count += j - i - 1
                i += 1
            return count >= k
        l = 0
        r = nums[-1] - nums[0]
        while l < r:
            m = l + (r-l)//2
            if enough(m):
                r = m
            else:
                l = m + 1
        return l
