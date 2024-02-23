class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = 0
        for i in s+t:
            d ^= ord(i)
        return chr(d)
