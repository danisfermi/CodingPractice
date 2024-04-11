class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m1 = {}
        m2 = {}
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        for i in range(len(s)):
            if s[i] in m1 and m1[s[i]] != pattern[i]:
                return False
            if pattern[i] in m2 and m2[pattern[i]] != s[i]:
                return False
            m1[s[i]] = pattern[i]
            m2[pattern[i]] = s[i]
        return True
