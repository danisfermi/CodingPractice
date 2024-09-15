'''
You work as a consultant and have clients in cityA and cityB. On a given day,
say i, you can either
work in cityA and make Ai dollars or you can work in cityB and make Bi dollars. You can also spend
the day traveling between cityA and cityB in which case your earnings that day are 0.
Given Al,A2, ....An and B1, B2,....., Bn, return a schedule S of N days which maximizes your earnings,
where S is a string of length N, and Si = A/B/T where A means work in cityA, B means work in cityB
T means travel on day i. You can start either in cityA or cityB. 
Example1: A = [23, 4,5 ,101] B = [21,1,10, 100] The optimal schedule S here would be ->"ATBB"
Example 2: A[25,10,15,10,70] B = [5,5,50,5,30] The optimal schedule S here would be-> "ATBTA"
'''

def helper(i, city, curr):
	if i == len(arr1):
		return (0, curr)
	work, path1 = helper(i+1, city, curr+("B" if city else "A"))
	travel, path2 = helper(i+1, not city, curr+"T")
	if arr1[i][city] + work > travel:
		return (arr1[i][city] + work, path1)
	else:
		return (travel, path2)

def schedule(arr):
	res1 = helper(0, 0, "")
	res2 = helper(0, 1, "")
	if res1 > res2:
		return res1[1]
	else:
		return res2[1]

'''
arr = [[23, 21],[4,1],[5,10],[101,100]]
print(schedule(arr))
'''
arr1 = [[25,5],[10,5],[15,50],[10,5],[70,30]]
print(schedule(arr1))
