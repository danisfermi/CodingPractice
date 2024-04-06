class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        st = []
        n = len(heights)
        for i in range(n):
            idx = i
            while st and st[-1][1] > heights[i]:
                idx, hi = st.pop()
                maxArea = max(maxArea, hi * (i - idx))
            st.append([min(idx, i), heights[i]])
        while st:
            idx, hi = st.pop()
            maxArea = max(maxArea, hi * (n - idx))
        return maxArea
            
