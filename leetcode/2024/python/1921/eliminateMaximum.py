class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        for d,s in zip(dist, speed):
            time.append(math.ceil(d/s))
        time.sort()
        res = 0
        for i in range(len(time)):
            if i >= time[i]:
                return res
            res += 1
        return res
