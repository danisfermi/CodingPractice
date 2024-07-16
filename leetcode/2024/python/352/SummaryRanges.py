from sortedcontainers import SortedDict

class SummaryRanges:

    def __init__(self):
        self.treemap = SortedDict()

    def addNum(self, value: int) -> None:
        self.treemap[value] = True

    def getIntervals(self) -> List[List[int]]:
        res = []
        for val in self.treemap:
            if res and res[-1][1]+1 == val:
                res[-1][1] = val
            else:
                res.append([val, val])
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals() 
