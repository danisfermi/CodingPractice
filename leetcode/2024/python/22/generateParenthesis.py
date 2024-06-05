class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(st, open, close):
            if open == n and close == n:
                res.append(st)
                return
            if open > n:
                return
            if close > open:
                return
            helper(st+"(", open+1, close)
            helper(st+")", open, close+1)
        helper("", 0, 0)
        return res
