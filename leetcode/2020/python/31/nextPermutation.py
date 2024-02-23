class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        def reverse(l, s):
            e = len(l)-1
            while s < e:
                temp = l[s]
                l[s] = l[e]
                l[e] = temp
                s += 1
                e -= 1
        i = len(nums)-2
        while i >=0 and nums[i+1] <= nums[i]:
            i -= 1
        if i >= 0:
            # Swap
            j = len(nums)-1
            while j >=0 and nums[j] <= nums[i]:
                idx = j
                j -= 1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            # Sort
        reverse(nums, i+1)
