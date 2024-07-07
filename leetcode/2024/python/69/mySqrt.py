class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        l = 1
        r = x
        while l < r:
            m = l + (r-l)//2
            if m*m > x:
                r = m
            else:
                l = m + 1
        return l-1
