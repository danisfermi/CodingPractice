class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        minHeap = []
        curCap = 0
        for c, i, j in trips:
            while minHeap and minHeap[0][0] <= i:
                curCap -= minHeap[0][1]
                heapq.heappop(minHeap)
            curCap += c
            if curCap > capacity:
                return False
            heapq.heappush(minHeap, (j, c))
        return True
