class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]
        for i in range(1, len(nums)):
            if currSum + nums[i] > nums[i]:
                currSum = currSum + nums[i]
            else:
                currSum = nums[i]
            maxSum = max(maxSum, currSum)
        return maxSum
