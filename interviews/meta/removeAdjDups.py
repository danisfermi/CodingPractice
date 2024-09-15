'''
You are given a String ("abbbaccaxa") represting a board game. Each time you play on board, you have to collapse all the contiguous duplicates. Return the final state when you cannot collapse any more characters in string;

Input: "axabbbacca"
Output: "axa" or "ax"

There are two ways to understand this question. Ask the interviewer which route they want to go. For first output the algo can be O(n) using stack or char with two pointers (simulate stack). The second output requires approach where you need to reparse the intermediate result after collapsing the duplicates, which, I think, best is O(n^2).

Input: "aaaaa"
Output: ""
'''

def removeDuplicates(input: str) -> str:
    if not input:
        return input
    
    stack = []
    stack.append([input[0], 1])
    
    for i in range(1, len(input)):
        if input[i] != input[i-1]:
            if stack[-1][1] >= 2:
                stack.pop()
            if stack and stack[-1][0] == input[i]:
                stack[-1][1] += 1
            else:
                stack.append([input[i], 1])
        else:
            stack[-1][1] += 1
            
    # handle end
    if stack[-1][1] >= 2:
        stack.pop()
        
    out = []
    for ltrs in stack:
        out += ltrs[0] * ltrs[1]
    
    return ''.join(out)

str = "axabbbacca"
print(removeDuplicates(str))
