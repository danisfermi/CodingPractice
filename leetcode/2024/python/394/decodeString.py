class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0
        
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == "[":
                stack.append(curr_num)
                stack.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif c == "]":
                prev_str = stack.pop()
                prev_num = stack.pop()
                curr_str = prev_str + curr_str * prev_num
            else:
                curr_str += c
        while stack:
            curr_str = stack.pop() + curr_str
        
        return curr_str
                
