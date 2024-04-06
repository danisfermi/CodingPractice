class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = 0
        arr = list(s)

        for i in range(len(arr)):
            if arr[i] == '(':
                left += 1
            elif arr[i] == ')':
                if left == 0:
                    arr[i] = '*'
                else:
                    left -= 1

        for i in range(len(arr) - 1, -1, -1):
            if left > 0 and arr[i] == '(':
                arr[i] = '*'
                left -= 1
        
        # Filter out marked characters and construct the result string
        result = ''.join(c for c in arr if c != '*')

        return result
        
        
