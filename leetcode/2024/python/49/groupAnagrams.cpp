class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        def getKey(word):
            res = [0] * 26
            for i in word:
                res[ord(i) - ord('a')] += 1
            return tuple(res)
        for word in strs:
            key = getKey(word)
            if key in m:
                m[key].append(word)
            else:
                m[key] = [word]
        res = []
        for i in m:
            res.append(m[i])
        return res
