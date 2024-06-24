class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def feasible(idx, l, r):
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    return True
                else:
                    return False
            else:
                if nums[mid] < target <= nums[r]:
                    return False
                else:
                    return True
        l = 0
        r = len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if feasible(mid, l, r):
                r = mid
            else:
                l = mid + 1
        return l if nums[l] == target else -1
