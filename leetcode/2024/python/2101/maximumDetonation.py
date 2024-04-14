class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x2-x1)**2 + (y2-y1)**2)
                if r1 >= d:
                    adj[i].append(j)
                if r2 >= d:
                    adj[j].append(i)
        res = 0
        def dfs(idx, visit):
            if idx in visit:
                return 0
            visit.add(idx)
            for nei in adj[idx]:
                dfs(nei, visit)
            return len(visit)
            
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))
        return res
