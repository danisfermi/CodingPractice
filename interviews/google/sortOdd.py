'''
Sort all odd elements and leave even elements as it is at their original position
e.g. [3,14,5,16,8,-2,3] ---> [3,14,3,16,8,-2,5] (note only 3,3,5 gets sorted and rest remained as it is)
'''

def partition(arr, start, end):
	pivot = arr[end]
	idx = start
	for i in range(start, end):
		if arr[i] <= pivot:
			arr[idx], arr[i] = arr[i], arr[idx]
			idx += 1
	arr[idx], arr[end] = arr[end], arr[idx]
	print("part ", arr)
	return idx

def quickSort(arr, start, end):
	if start < end:
		pi = partition(arr, start, end)
		quickSort(arr, start, pi-1)
		quickSort(arr, pi+1, end)


def sortOdd(arr):
	odd = []
	for i in range(len(arr)):
		if arr[i] % 2 == 1:
			odd.append(arr[i])
	quickSort(odd, 0, len(odd)-1)

	idx = 0
	for i in range(len(arr)):
		if arr[i] % 2 == 1:
			arr[i] = odd[idx]
			idx += 1
	return arr


input = [3,14,5,16,8,-2,3,1,5,6,8,9,11]
print(sortOdd(input))
