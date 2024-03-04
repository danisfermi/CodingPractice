class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        l = 0
        r = len(tokens)-1
        tokens.sort()
        while l <= r and (score or power >= tokens[l]):
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
            elif r != l:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        return score
                
