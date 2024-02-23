class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binSearch(nums, l, r, target):
            if l > r:
                return -1
            if l == r and nums[l] != target:
                return -1
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    return binSearch(nums, l, mid-1, target)
                return binSearch(nums, mid+1, r, target)
            else:
                if target > nums[mid] and target <= nums[r]:
                    return binSearch(nums, mid+1, r, target)
                return binSearch(nums, l, mid-1, target)          
        return binSearch(nums, 0 , len(nums)-1, target)
