class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n):
            if n == 0:
                return 1
            if n == 1:
                return x
            res = helper(n//2)
            return res * res if n % 2 == 0 else (res * res * x)
        res = helper(abs(n))
        return res if n > 0 else (1/res)
