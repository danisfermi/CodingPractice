class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def helper(l, idx):
            if idx >= len(nums):
                self.res.append(l.copy())
                return
            l.append(nums[idx])
            helper(l, idx + 1)
            l.pop()
            helper(l, idx + 1)
        helper([], 0)
        return self.res
