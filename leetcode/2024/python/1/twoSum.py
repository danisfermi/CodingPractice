class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, j in enumerate(nums):
            s = target - j
            if s in m:
                return [m[s], i]
            m[j] = i
        return []
