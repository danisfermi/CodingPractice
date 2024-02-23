class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        def myFunc(e):
            return e[1]
        intervals.sort(key=myFunc)
        count = 0
        prev_end = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < prev_end:
                count += 1
            else:
                prev_end = intervals[i][1]
        return count
