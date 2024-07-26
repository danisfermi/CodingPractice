class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(dots, i, curr):
            if i == len(s) and dots == 4:
                res.append(curr[:-1])
            if dots > 4:
                return
            for x in range(i, min(i+3, len(s))):
                ans = s[i:x+1]
                if int(s[i:x+1]) <= 255 and (i == x or s[i] != "0"):
                    backtrack(dots+1, x+1, curr+ans+".")
                
        backtrack(0, 0, "")
        return res
