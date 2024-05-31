class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j] += (int(num1[i]) * int(num2[j]))
                carry = res[i+j]//10
                res[i+j] = res[i+j]%10
                res[i+j+1] += carry
        res = res[::-1]
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)
