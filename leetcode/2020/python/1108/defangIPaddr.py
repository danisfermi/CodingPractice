class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        res = ""
        for i in address:
            if i == ".":
                res += "[.]"
            else:
                res += i
        return res
