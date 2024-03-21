class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s) - 1
        res = 0
        while j >= 0:
            if s[j] != " ":
                break
            j -= 1
        while j >= 0:
            if s[j] == " ":
                break
            res += 1
            j -= 1
        return res
