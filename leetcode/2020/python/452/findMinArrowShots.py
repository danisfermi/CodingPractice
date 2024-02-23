class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        def myFunc(e):
            return e[1]
        points.sort(key=myFunc)
        count = 1
        arrowPos = points[0][1]
        for j in range(1,len(points)):
            if arrowPos < points[j][0]:
                count += 1
                arrowPos = points[j][1]
            else:
                arrowPos = min(arrowPos, points[j][1])
        return count
