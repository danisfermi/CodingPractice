class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n 
        prices[src] = 0

        for i in range(k + 1) :
            tempprices = prices.copy()
            for s ,d , p in flights :
                if prices[s] == float("inf") :
                    continue
                if prices[s] + p < tempprices[d] :
                    tempprices[d] = prices[s] + p
            prices = tempprices
        if prices[dst] == float("inf") :
            return -1
        else :
            return prices[dst]
