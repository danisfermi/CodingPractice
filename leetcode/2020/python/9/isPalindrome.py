class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        divisor = 1
        while x / divisor >= 10:
            divisor *= 10
        while x != 0:
            first = x / divisor
            last = x % 10
            if first != last:
                return False
            x = (x % divisor) / 10
            divisor = divisor / 100
        return True
