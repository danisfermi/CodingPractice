class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        pq = [-c for c in count.values()]
        heapq.heapify(pq)
        time = 0
        q = []
        while pq or q:
            time += 1
            if pq:
                cnt = 1 + heapq.heappop(pq)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(pq, q.pop(0)[0])      
        return time
