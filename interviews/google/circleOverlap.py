import math
'''
Problem: A circle is define by x-axis position, y-axis position, and a
radius. A circle group is a collection of circles that overlap. Given a
list of circles, figure out if they belong to a single circle group
'''

class UnionFind:
	def __init__(self, n):
		self.parent = [i for i in range(n)]
		self.rank = [1] * n
		self.components = n

	def find(self, x):
		node = x
		while node != self.parent[node]:
			node = self.parent[node]
			self.parent[node] = self.parent[self.parent[node]]
		return node

	def union(self, x, y):
		px, py = self.find(x), self.find(y)
		if px == py:
			return False
		if self.rank[px] > self.rank[py]:
			self.parent[py] = px
			self.rank[px] += self.rank[py]
		else:
			self.parent[px] = py
			self.rank[py] += self.rank[px]
		self.components -= 1
		return True

def overlap(arr):
	uf = UnionFind(len(arr))	
	circles = []
	for i in range(len(arr)):
		c1 = arr[i]
		for j in range(i+1, len(arr)):
			c2 = arr[j]
			distance = math.sqrt((c2[0] - c1[0]) * (c2[0] - c1[0]) + (c2[1] - c1[1]) * (c2[1] - c1[1]))
			# overlap if distance between centers is less than sum of radius
			if distance < (c2[2] + c1[2]):
				circles.append([i, j])
	for i, j in circles:
		uf.union(i, j)
	return uf.components == 1
			

arr = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
print(overlap(arr))

arr = [[1,1,5],[10,10,5]]
print(overlap(arr))

