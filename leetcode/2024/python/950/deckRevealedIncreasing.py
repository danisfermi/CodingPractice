class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        queue = deque()

        for i in range(N):
            queue.append(i)
        
        deck.sort()

        result = [0] * N
        for card in deck:
            result[queue.popleft()] = card

            if queue:
                queue.append(queue.popleft())
                
        return result
