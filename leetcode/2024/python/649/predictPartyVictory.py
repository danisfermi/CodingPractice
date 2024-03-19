class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        for j, i in enumerate(senate):
            if i == "R":
                radiant.append(j)
            else:
                dire.append(j)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(r + len(senate))
            else:
                dire.append(d + len(senate))
        return "Radiant" if radiant else "Dire"
