class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = n
        for i in xrange(1,n):
            l = i-1
            h = i
            while l >= 0 and h < len(s) and s[l] == s[h]:
                res += 1
                l -= 1
                h += 1
            l = i-1
            h = i+1
            while l >= 0 and h < len(s) and s[l] == s[h]:
                res += 1
                l -= 1
                h += 1
        return res
