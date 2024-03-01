class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l = [ c for c in s]
        left = 0
        for right in range(len(l)):
            if l[right] == "1":
                l[right], l[left] = l[left], l[right]
            if l[left] == "1":
                left += 1
        l[len(l)-1], l[left-1] = l[left-1], l[len(l)-1]
        return "".join(l)
