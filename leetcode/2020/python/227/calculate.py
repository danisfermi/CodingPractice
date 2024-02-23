class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if len(s) == 0:
            return 0
        currNum = 0
        lastNum = 0
        sign = "+"
        res = 0
        for i in xrange(n):
            char = s[i]
            if char.isdigit():
                currNum = (currNum * 10) + int(char)
            if ((char.isdigit() == 0 and char != " ") or i == (n - 1)):
                if sign == "+" or sign == "-":
                    res += lastNum
                    lastNum = (currNum if sign == "+" else -currNum)
                elif sign == "*":
                    lastNum = lastNum * currNum
                elif sign == "/":
                    lastNum = abs(lastNum) / abs(currNum) * (-1 if lastNum <= 0 or currNum <= 0 else 1)
                sign = char
                currNum = 0
        return (res + lastNum)
