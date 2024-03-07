class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = 0
        currMin = 0
        globMax = nums[0]
        globMin = nums[0]
        total = 0
        for n in nums:
            currMax = max(currMax+n, n)
            currMin = min(currMin+n, n)
            globMax = max(globMax, currMax)
            globMin = min(currMin, globMin)
            total += n
        return max(globMax, total - globMin) if globMax >= 0 else globMax
