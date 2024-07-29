class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            if n % 2 == 0:
                res += int(n / 2)
                n = n/2
            else:
                res += int((n-1)/2)
                n = ((n-1)/2) + 1
        return res
        
