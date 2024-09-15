'''
Identify underpaid managers/employees

You are given a class representing employees, where each employee has a salary and a list of subordinates. The subordinates can further have their subordinates, forming a hierarchical employee structure. Given a root employee as input, write a program that lists employees who are managers and have a salary lower than the average salary of their subordinates.
For example:
- Emp1 (85k)
    +- Emp2 (90k)
        +- Emp3 (170k)
        +- Emp4 (60k)
    +- Emp2 (70k)
        +- Emp5 (50k)
In the provided example, since EMP2 has salary lower than the average of its subordinates, EMP3 and EMP4, EMP2 is considered an underpaid employee. Similarly, since EMP1 has salary lower than all of its subordinates, EMP1 is also classified as an underpaid employee.
'''

from collections import defaultdict

adj = defaultdict(list)
visit = set()

def helper(node):
	if node in visit:
		return (0, 0)
	visit.add(node)
	totSal = 0
	totCnt = 0
	for child in adj[node]:
		sal, cnt = helper(child)
		totSal += sal
		totCnt += cnt
		if salaries[node] < totSal/totCnt:
			print(node, " is underpaid.")
	return (totSal+salaries[node], totCnt+1)

def countManagers():
	res = 0
	for i,j in map:
		adj[i].append(j)
	helper("A")
'''
map = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E')]
salaries = {'A': 50000, 'B': 20000, 'C': 10000, 'D': 10000, 'E': 25000}
'''

map = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F')]
salaries = {'A': 85, 'B': 90, 'C': 70, 'D': 170, 'E': 60, 'F': 50}
countManagers()
