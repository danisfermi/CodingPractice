class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ones = 0
        zero = 0
        res = 0
        m = {}
        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                ones += 1
            diff = ones - zero
            if diff not in m:
                m[diff] = i
            if ones == zero:
                res = ones + zero
            else:
                idx = m[diff]
                res = max(res, i - idx)
        return res
