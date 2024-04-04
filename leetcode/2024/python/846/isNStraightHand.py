class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hasho = Counter(hand)
        keys = sorted(hasho)

        for key in keys:
            if hasho[key] > 0:
                for i in range(groupSize-1, -1, -1):
                    if key+i not in hasho:
                        return False

                    hasho[key+i] -= hasho[key]
                    
                    if hasho[key+i] < 0:
                        return False 

        return True 
