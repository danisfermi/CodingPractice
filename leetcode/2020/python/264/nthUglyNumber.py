class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0,0,0]
        ug = [1]
        while n > 1:
            u1 = ug[arr[0]] * 2
            u2 = ug[arr[1]] * 3
            u3 = ug[arr[2]] * 5
            ug.append(min(u1, u2, u3))
            if ug[-1] == u1:
                arr[0] += 1
            if ug[-1] == u2:
                arr[1] += 1
            if ug[-1] == u3:
                arr[2] += 1
            n -= 1
        return ug[-1]
