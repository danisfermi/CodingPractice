class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        res = 0
        pro = 1
        while r < len(nums):
            pro *= nums[r]
            while l <= r and pro >= k:
                pro /= nums[l]
                l += 1
            res += (r-l+1)
            r += 1
        return res
