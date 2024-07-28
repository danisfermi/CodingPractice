class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        for n in nums:
            n = abs(n)
            nums[n-1] *= -1
            if nums[n-1] > 0:
                res[0] = n
        for i, n in enumerate(nums):
            if n > 0 and res[0] != i+1:
                res[1] = i+1
                return res
