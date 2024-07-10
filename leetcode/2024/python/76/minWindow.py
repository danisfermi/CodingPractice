class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapT = {}
        for i in t:
            mapT[i] = mapT.get(i, 0) + 1
        have = 0
        need = len(mapT)
        res = ""
        resLen = float('inf')
        mapS = {}
        l = 0
        for r in range(len(s)):
            c = s[r]
            mapS[c] = 1 + mapS.get(c, 0)
            if c in mapT and mapS[c] == mapT[c]:
                have += 1
            while have == need:
                if resLen > r - l + 1:
                    res = s[l:r+1]
                    resLen = r - l + 1
                mapS[s[l]] -= 1
                if s[l] in mapT and mapS[s[l]] < mapT[s[l]]:
                    have -= 1
                l += 1
        return res
