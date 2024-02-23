class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_max = nums[0]
        max_end = nums[0]
        for i in range(1,len(nums)):
            sum_max = max(nums[i], sum_max+nums[i])
            max_end  = max(max_end, sum_max)
        return max_end
