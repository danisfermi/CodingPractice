class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]
        min_so_far = nums[0]
        pro_so_far = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                temp = max_so_far
                max_so_far = min_so_far
                min_so_far = temp
            max_so_far = max(nums[i], max_so_far*nums[i])
            min_so_far = min(nums[i], min_so_far*nums[i])
            pro_so_far = max(pro_so_far, max_so_far)
        return pro_so_far
