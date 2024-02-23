class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        k = keysPressed[0]
        t = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            diff = releaseTimes[i] - releaseTimes[i-1]
            if diff > t or (diff == t and keysPressed[i] > k):
                k = keysPressed[i]
                t = diff
        return k
