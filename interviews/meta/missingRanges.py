'''
Given an array of integers with a lower bound of 0 and upper bound of 99, return a comma delimited string of all missing integers. If the difference between two integers in the string is greater than 2, use a dash.
example:
input: [1,2,4,7,55,95]
output: "0,3,5,6,8-54,56-94,96-99"
'''

def missingRanges(nums):
    lower = 0
    upper = 99
    
    num_elements = len(nums)

    if num_elements == 0:
        return [[lower, upper]]

    missing_ranges = []

    if nums[0] > lower:
        missing_ranges.append([lower, nums[0] - 1])

    for i in range(len(nums)-1):
        a = nums[i]
        b = nums[i+1]
        if b - a > 1:
            missing_ranges.append([a + 1, b - 1])

    if nums[-1] < upper:
        missing_ranges.append([nums[-1] + 1, upper])

    res = ""
    for i in missing_ranges:
        if i[0] == i[1]:
            res += str(i[0]) + ","
        else:
            res += str(i[0]) + "-" + str(i[1]) + ","
    return res

input = [1,2,4,7,55,95]
print(missingRanges(input))
