class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)
        while l < r:
            m = l + (r-l)//2
            if nums[m] >= target:
                r = m
            else:
                l = m+1
        return l
