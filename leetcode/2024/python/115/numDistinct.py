class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def helper(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            res = 0
            if s[i] != t[j]:
                res = helper(i+1, j)
            else:
                res = helper(i+1, j+1) + helper(i+1, j)
            cache[(i, j)] = res
            return res
        return helper(0, 0)
