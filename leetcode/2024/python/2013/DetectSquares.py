class DetectSquares:

    def __init__(self):
        self.points = []
        self.pntCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pntCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x, y in self.points:
            if (abs(py-y) != abs(px-x)) or (px == x) or (py == y):
                continue
            res += (self.pntCount[(x, py)] * self.pntCount[px, y])
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
