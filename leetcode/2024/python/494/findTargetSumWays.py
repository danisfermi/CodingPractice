class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def helper(i, total):
            if (i, total) in cache:
                return cache[(i, total)]
            if total == target and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            cache[(i, total)] = helper(i+1, total + nums[i]) + helper(i+1, total - nums[i])
            return cache[(i, total)]
        return helper(0, 0)
