class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        l = len(grid[0])
        preRow1 = grid[0].copy()
        preRow2 = grid[1].copy()
        for i in range(1, l):
            preRow1[i] += preRow1[i-1]
            preRow2[i] += preRow2[i-1]
        res = float('inf')
        for i in range(l):
            top = preRow1[-1] - preRow1[i]
            bottom = preRow2[i-1] if i > 0 else 0
            secondRobot = max(top, bottom)
            res = min(res, secondRobot)
        return res
            
