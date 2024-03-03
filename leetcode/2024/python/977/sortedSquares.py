class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l = 0
        r = len(nums)-1
        while l <= r:
            left = nums[l] ** 2
            right = nums[r] ** 2
            if left >= right:
                res.append(left)
                l += 1
            else:
                res.append(right)
                r -= 1
        return res[::-1]
