class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def isPal(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        def dfs(idx):
            if idx == len(s):
                res.append(part.copy())
                return
            for i in range(idx, len(s)):
                if isPal(s, idx, i):
                    part.append(s[idx:i+1])
                    dfs(i+1)
                    part.pop()
        dfs(0)
        return res
    
