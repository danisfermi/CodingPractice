class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(idx, curr, total):
            if total == target:
                res.append(curr[::])
                return
            if total > target or idx >= len(candidates):
                return
            curr.append(candidates[idx])
            dfs(idx+1, curr, total+candidates[idx])
            k = 1
            while idx+k < len(candidates) and candidates[idx+k] == candidates[idx]:
                k += 1
            curr.pop()
            dfs(idx+k, curr, total)
        dfs(0, [], 0)
        return res
