class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        R = 0
        L = 0
        count = 0
        for i in range(0, len(s)):
            if s[i] == "R":
                R += 1
            elif s[i] == "L":
                L += 1
            if R == L:
                count += 1
                R, L = 0, 0
        return count
