class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        mHeap = [[grid[0][0], 0, 0]]
        dirs = [[0,1], [1,0], [-1,0],[0,-1]]
        N = len(grid)
        visit = set()
        visit.add((0, 0))
        while mHeap:
            mH, row, col = heapq.heappop(mHeap)
            if (row == N - 1) and (col == N - 1):
                return mH
            for dr, dc in dirs:
                neir, neic = row+dr, col+dc
                if neir < 0 or  neic < 0 or neir == N or neic == N or (neir, neic) in visit:
                    continue
                visit.add((neir, neic))
                heapq.heappush(mHeap, (max(mH, grid[neir][neic]), neir, neic))
        return -1
        
