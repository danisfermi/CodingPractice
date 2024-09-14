'''
You have a stream of rpc requests coming in. Each log is of the form {id, timestamp, type(start/end)}. Given a timeout T, you need to figure out at the earliest possible time if a request has timed out.
Eg :
id - time - type
0 - 0 - Start
1 - 1 - Start
0 - 2 - End
2 - 6 - Start
1 - 7 - End
Timeout = 3
Ans : {1, 6} ( figured out id 1 had timed out at time 6 )
'''
from collections import deque

timeout = 3
map = {}
q = deque()
def rpcStream(req):
	for r in req:
		if r[2] == "start":
			map[r[0]] = r[1]
			q.append(r[0])
		else:
			id, endTime, _ = r
			startTime = map[id]
			if endTime - startTime > timeout:
				return (id, startTime, endTime)
			del map[id]
		while q and q[0] not in map:
			q.popleft()
		if q and r[1] - map[q[0]] > timeout:
			return (q[0], map[q[0]], r[1])  
	return [-1, -1, -1]

# id, time, category
input = [[0, 0, "start"],[1, 1, "start"],[0, 2, "end"],[2, 6, "start"],[1, 7, "end"]]
print(rpcStream(input))
