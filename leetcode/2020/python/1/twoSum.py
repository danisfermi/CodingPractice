class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        res =[]
        for i in range(0, len(nums)):
            rem = target - nums[i]
            if rem in m:
                res.append(i)
                res.append(m[rem])
                return res
            m[nums[i]] = i
