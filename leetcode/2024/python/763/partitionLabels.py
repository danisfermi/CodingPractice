class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        for i, c in enumerate(s):
            count[c] = i
        size = 0
        end = 0
        res = []
        for i, c in enumerate(s):
            size += 1
            end = max(end, count[c])
            if i == end:
                res.append(size)
                size = 0
        return res
