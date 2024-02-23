class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = {}
        for i in s:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        for i in t:
            if i not in m:
                return False
            m[i] -= 1
        for i in m:
            if m[i] != 0:
                return False
        return True
