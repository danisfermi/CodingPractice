'''
Give a list of string, where every string in the list is of size 5.
Return the list of 5 string such that all the characters in each of the strings are unique
i.e if we combine all the strings(not nnecessary) we will have 25 unique characters)
eg
Input explanation
List of string with length of 5 each
input = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "zabcd", "apple", "zebra", "ocean", "quick", "world", "jumps", "foxes", "liver"]

all the 5 string have unique character for both of the way
output = ["abcde", "fghij", "klmno", "pqrst", "uvwxy"] or ["fghij", "klmno", "pqrst", "uvwxy", "zabcd"]
'''

res = []
def backtrack(idx, charSet, curr):
	if len(curr) == 5:
		if len(charSet) == 25:
			res.append(curr.copy())	
			return
	if idx == len(input):
		return

	for i in range(idx, len(input)):
		temp = curr
		valid = True
		tempCharSet = charSet
		st = input[i]
		for c in st:
			if c in tempCharSet:
				valid = False
				break
			tempCharSet.add(c)

		if valid:
			temp.append(st)
			backtrack(idx+1, tempCharSet, temp)	
			if res:
				return


input = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "zabcd", "apple", "zebra", "ocean", "quick", "world", "jumps", "foxes", "liver"]
backtrack(0, set(), [])
print(res)
