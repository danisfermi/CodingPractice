'''
There is a robot at location (0, 0) of a 10x10 grid of tiles. Each tile can be one of 8 different colors: (0, 1, ... 7). There is a star at a known location (marked with the color -1) on the grid. You can program the robot by giving it a lookup table of color to direction. The robot will sense the color of the tile it is currently on, and move in the direction (up, down, left, or right) specified by the lookup table you provided. Output a lookup table that guides the robot to the star, if such a table is possible.

Small example grid:
[[(0), 1,  0,  0],
 [3,   2, -1,  3],
 [0,   0,  0,  2],
 [0,   0,  0,  4]]
Solution:
0: Right, 1: Down, 2: Left, 3: Up
'''

def get_lookup_table(grid):
	ROWS = len(grid)
	COLS = len(grid[0])
	dirs = [[-1, 0], [1,0], [0,1], [0,-1]]
	lookupTbl = {}
	visited = set()
	def dfs(r, c):
		if r < 0 or r >= ROWS or c >= COLS or c < 0:
			return False
		color = grid[r][c]
		if color == -1:
			return -1
		if color in lookupTbl:
			dr, dc = lookupTbl[color]
			nrow, ncol = r + dr, c + dc
			if (nrow, ncol) not in visited:
				visited.add((nrow, ncol))
				if dfs(nrow, ncol):
					return True
				visited.remove((nrow, ncol))
		else:
			for dr, dc in dirs:
				lookupTbl[color] = (dr, dc)
				if dfs(r, c):
					return True
				lookupTbl.pop(color)
		return False
	if dfs(0, 0):
		return lookupTbl

grid = [
        [0,   1,  0,  0],
        [3,   2, -1,  3],
        [0,   0,  0,  2],
        [0,   0,  0,  4]
    ]
lookup_table = get_lookup_table(grid)
print(lookup_table)
