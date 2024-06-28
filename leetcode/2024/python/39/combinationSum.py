class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        def helper(temp, idx, s):
            if s == target:
                self.res.append(temp.copy())
                return
            if idx >= len(candidates) or s > target:
                return
            temp.append(candidates[idx])
            helper(temp, idx, s + candidates[idx])
            temp.pop()
            helper(temp, idx+1, s)
        helper([], 0, 0)
        return self.res
            
