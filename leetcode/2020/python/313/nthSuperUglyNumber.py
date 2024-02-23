class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ug = [1]
        arr = [0] * (len(primes))
        ux = [0] * (len(primes))
        while n > 1:
            for x in range(0,len(primes)):
                ux[x] = ug[arr[x]] * primes[x]
            ug.append(min(ux))
            for x in range(0,len(primes)):
                if ug[-1] == ux[x]:
                    arr[x] += 1
            n -= 1
        return ug[-1]
