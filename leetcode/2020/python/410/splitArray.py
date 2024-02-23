class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def feasible(mid):
            total = 0
            count = 1
            for i in nums:
                total += i
                if total > mid:
                    count += 1
                    total = i
                    if count > m:
                        return False
            return True
                
        l = max(nums)
        r = sum(nums)
        while l < r:
            mid = l + (r-l)//2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l
