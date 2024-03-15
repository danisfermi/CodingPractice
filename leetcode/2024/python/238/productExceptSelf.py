class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        proTillNow = 1
        res = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            proTillNow *= nums[i-1]
            res[i] = proTillNow
        proTillNow = 1
        for i in range(len(nums)-2, -1, -1):
            proTillNow *= nums[i+1]
            res[i] *= proTillNow
        return res
