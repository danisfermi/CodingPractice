class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        m = {}
        maxFreq = 0
        res = 0
        for n in nums:
            m[n] = m.get(n, 0) + 1
            freq = m[n]
            if freq > maxFreq:
                maxFreq = freq
                res = freq
            elif freq == maxFreq:
                res += freq
        return res
            
