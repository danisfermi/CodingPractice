class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        bar = 0
        for i, v in enumerate(nums):
            if i+v > bar:
                pre = bar
                bar = i+v
                for j in range(pre+1, min(bar+1, len(nums))):
                    dp[j] = dp[i] + 1
        return dp[-1]
