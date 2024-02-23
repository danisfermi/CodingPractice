class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        maxV = v = min(height[l], height[r]) * (r-l)
        while l < r:
            v = min(height[l], height[r]) * (r-l)
            if v > maxV:
                maxV = v
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxV
