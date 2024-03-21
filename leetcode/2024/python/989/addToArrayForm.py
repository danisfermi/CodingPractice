class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = 0
        num.reverse()
        while k:
            rem = k % 10
            if i < len(num):
                num[i] = num[i] + rem
            else:
                num.append(rem)
            carry = num[i] // 10
            num[i] = num[i] % 10
            i += 1
            k = k // 10
            k += carry
        num.reverse()
        return num
