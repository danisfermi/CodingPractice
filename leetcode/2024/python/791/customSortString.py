class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = collections.Counter(s)
        result = []
        for char in order:
            result.append(char * count.pop(char, 0))     
        for char, cnt in count.items():
            result.append(char * cnt)
        return ''.join(result)
