class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr_max = 0
        res = 0
        for n in nums:
            if n > curr_max:
                curr_max = n
                size = 1
                res = 0
            elif n == curr_max:
                size += 1
            else:
                size = 0
            res = max(res, size)
        return res
        '''
        curr_max = max(nums)
        curr = 0
        res = 0
        for i in nums:
            if i == curr_max:
                curr += 1
            else:
                curr = 0
            res = max(res, curr)
        return res   
        '''
