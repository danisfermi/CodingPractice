class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 1
        ans = s[0]
        for i in xrange(1,len(s)):
            low = i-1
            high = i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if high - low + 1 > maxLen:
                    ans = s[low:high+1]
                    maxLen = high-low+1
                low -= 1
                high += 1
            low = i-1
            high = i+1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if high - low + 1 > maxLen:
                    ans = s[low:high+1]
                    maxLen = high-low+1
                low -= 1
                high += 1
        return ans
