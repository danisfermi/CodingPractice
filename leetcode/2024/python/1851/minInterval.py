class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = {}
        i = 0
        mh = []
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(mh, (r - l + 1, r))
                i += 1
            while mh and mh[0][1] < q:
                heapq.heappop(mh)
            res[q] = mh[0][0] if mh else -1
        return [res[q] for q in queries]
