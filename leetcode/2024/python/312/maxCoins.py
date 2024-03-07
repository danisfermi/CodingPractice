class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}
        def helper(l ,r):
            if l > r:
                return 0
            if (l,r) in cache:
                return cache[(l ,r)]
            cache[(l, r)] = 0
            for i in range(l, r+1):
                coins = nums[i] * nums[l-1] * nums[r+1]
                coins += helper(l, i-1) + helper(i+1, r)
                cache[(l, r)] = max(coins, cache[(l, r)])
            return cache[(l, r)]
        return helper(1, len(nums)-2)
