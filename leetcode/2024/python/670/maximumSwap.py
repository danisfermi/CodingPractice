class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        for i in range(n-1):
            if s[i] < s[i+1]: break
        else: return num
        max_idx, max_val = i+1, s[i+1]
        for j in range(i+1, n):
            if max_val <= s[j]: max_idx, max_val = j, s[j]
        left_idx = i
        for j in range(i, -1, -1):    
            if s[j] < max_val: left_idx = j
        s[max_idx], s[left_idx] = s[left_idx], s[max_idx]
        return int(''.join(s))
            
