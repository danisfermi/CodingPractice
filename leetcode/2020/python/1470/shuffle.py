class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i1 in range(0,n):
            i2 = i1+n
            res.append(nums[i1])
            res.append(nums[i2])
        return res
