class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        first = points[0]
        res = len(points)
        for i in range(1,len(points)):
            second = points[i]
            if second[0] <= first[1]:
                res -= 1
                first[0] = max(first[0], second[0])
                first[1] = min(first[1], second[1])
            else:
                first = second
        return res
