class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        cache = {}
        MOD = 10**9 + 7
        def helper(target, d):
            if (target, d) in cache:
                return cache[(target, d)]
            if d == 0:
                return 1 if target == 0 else 0
            res = 0
            for i in range(1, k+1):
                res = (res + helper(target - i, d-1)) % MOD
            cache[(target, d)] = res
            return res
        return helper(target, n)
