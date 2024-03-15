class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(target):
            if target < 0:
                return 0
            l = 0
            currSum = 0
            res = 0
            for r in range(len(nums)):
                currSum += nums[r]
                while currSum > target:
                    currSum -= nums[l]
                    l += 1
                res += (r - l + 1)
            return res
        return helper(goal) - helper(goal - 1)
