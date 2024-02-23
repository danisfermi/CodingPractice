class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        st = 0
        m = {}
        l = 0
        for i in range(0,len(s)):
            if s[i] in m.keys():
                st = max(m[s[i]], st)
            l = max(l, i - st + 1)
            m[s[i]] = i + 1
        return l
