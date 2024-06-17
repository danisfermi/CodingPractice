class Solution:
    def isValid(self, s: str) -> bool:
        m = {')':'(', '}':'{', ']':'['}
        st = []
        for i in s:
            if i in ['(', '{', '[']:
                st.append(i)
            else:
                if i not in [')', '}', ']']:
                    return False
                else:
                    if not st:
                        return False
                    if st and st.pop() !=  m[i]:
                        return False
        return True if len(st) == 0 else False
