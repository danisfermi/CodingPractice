#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinimumOperations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''
1 2 1
1 3 5 2 2
    lr
l = 2
arr[l] = 4
left = 4
r = 2
arr[r] = 2
right = 4
res = 2
Time COmplexity: O(n)
Space: O(1)
'''



def getMinimumOperations(arr):
    # Write your code here
    l = 0
    r = len(arr) - 1
    res = 0
    # no negative elements in array
    # always possible
    while l < r:
        if arr[l] < arr[r]:
            left = arr[l]
            while l < r and left < arr[r]:
                res += 1
                l += 1
                left += arr[l]
            if left != arr[r]:
                arr[l] = left
                continue
        elif arr[l] > arr[r]:
            right = arr[r]
            while l < r and right < arr[l]:
                res += 1
                r -= 1
                right += arr[r]
            if right != arr[l]:
                arr[r] = right
                continue
        l += 1
        r -= 1
    return res
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getMinimumOperations(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
