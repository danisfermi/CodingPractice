class Solution:
    def maximum69Number (self, num: int) -> int:
        strNum = str(num)
        for x in range(len(strNum)):
            if strNum[x] == "6":
                strNum = strNum[:x]+"9"+strNum[x+1:]
                return int(strNum)
        return num
        
