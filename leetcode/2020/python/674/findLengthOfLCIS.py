class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        curr = 1
        max_curr = 1
        for i in range(1, len(nums)):
            print nums[i]
            if nums[i] > nums[i-1]:
                curr += 1
                max_curr = max(max_curr, curr)
            else:
                curr = 1
        return max_curr
