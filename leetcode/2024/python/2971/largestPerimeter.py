class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        res = 0
        for i in range(len(nums)): 
            if nums[i] < total:
                res = total + nums[i]
            total += nums[i]
        return res if res else -1
