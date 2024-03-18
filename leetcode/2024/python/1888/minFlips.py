class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        str1 = ""
        str2 = ""
        s = s + s
        for i in range(len(s)):
            str1 += "1" if i % 2 else "0"
            str2 += "0" if i % 2 else "1"
        res = len(s)
        diff1 = 0
        diff2 = 0
        l = 0
        for r in range(len(s)):
            if s[r] != str1[r]:
                diff1 += 1
            if s[r] != str2[r]:
                diff2 += 1
            if (r - l + 1) > n:
                if s[l] != str1[l]:
                    diff1 -= 1
                if s[l] != str2[l]:
                    diff2 -= 1
                l += 1
            if (r - l + 1) == n:
                res = min(res, diff1, diff2)
        return res
