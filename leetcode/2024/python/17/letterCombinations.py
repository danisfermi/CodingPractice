class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        m = {}
        m['2'] = "abc"
        m['3'] = "def"
        m['4'] = "ghi"
        m['5'] = "jkl"
        m['6'] = "mno"
        m['7'] = "pqrs"
        m['8'] = "tuv"
        m['9'] = "wxyz"
        
        def dfs(idx, temp):
            if len(temp) == len(digits):
                res.append(temp)
                return
            for i in m[digits[idx]]:
                dfs(idx+1, temp+i)
        if digits:
            dfs(0, "")
        return res
