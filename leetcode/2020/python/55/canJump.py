class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pos = len(nums)-1
        for i in xrange(len(nums)-1,-1,-1):
            if i + nums[i] >= pos:
                pos = i
        if pos == 0:
            return True
        else:
            return False
