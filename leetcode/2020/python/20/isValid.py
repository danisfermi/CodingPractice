class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        m = {}
        m["]"] = "["
        m[")"] = "("
        m["}"] = "{"
        for i in s:
            if i in ["[", "(", "{"]:
                st.append(i)
            else:
                if len(st) and st[-1] == m[i]:
                    st.pop()
                else:
                    st.append(i)
        if len(st) == 0:
            return True
        else:
            return False
