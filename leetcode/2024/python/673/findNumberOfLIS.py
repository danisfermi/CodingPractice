class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        res = 0
        lenLIS = 0
        for i in range(len(nums)-1, -1, -1):
            maxLen = 1
            maxCnt = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    Len, Cnt = dp[j]
                    if Len + 1 > maxLen:
                        maxLen = Len + 1
                        maxCnt = Cnt
                    elif Len + 1 == maxLen:
                        maxCnt += Cnt
            if maxLen > lenLIS:
                lenLIS = maxLen
                res = maxCnt
            elif maxLen == lenLIS:
                res += maxCnt
            dp[i] = [maxLen, maxCnt]
        return res
