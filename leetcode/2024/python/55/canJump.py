class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True

        for i in range(1,len(nums)):
            for j in range(i-1,-1,-1):
                if nums[j] >= i - j and dp[j]:
                    dp[i] = True
                    break

        return dp[-1]
