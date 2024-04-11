class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        remain = len(num) - k
        for digit in num:
            while k and st and st[-1] > digit:
                st.pop()
                k -= 1
            st.append(digit)
        return ''.join(st[:remain]).lstrip('0') or '0'
