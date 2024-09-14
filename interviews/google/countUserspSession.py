'''
Question:
You are given a list of user sessions where each user session has start and end times both inclusive. Now, given a value N, find the count of all users at each point in time from [0,N) i.e include 0 but exclude N.
Example:
Input:
[(0,3), (1,4) ], N = 7
Output:
0->1
1->2
2->2
3->2
4->1
5->0
6->0
PS: Assume all inputs are valid.
'''

def findUserspSession(arr, n):
	res = [0] * n
	for start, end in arr:
		res[start] += 1
		if end + 1 < n:
			res[end+1] -= 1
	for i in range(1, n):
		res[i] += res[i-1]	
	return res

arr = [[0, 3], [1, 4]] 
print(findUserspSession(arr, 7))
