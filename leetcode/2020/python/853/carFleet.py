class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position,speed))
        times = [float(target - p) / s for p, s in cars]
        count = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]:
                count += 1
            else:
                times[-1] = lead
        return count + bool(times)
