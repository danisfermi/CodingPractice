class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums.copy()]
        res = []
        for i in range(len(nums)):
            el = nums.pop(0)
            perms = self.permute(nums)
            for p in perms:
                p.append(el)
            res.extend(perms)
            nums.append(el)
        return res
        
