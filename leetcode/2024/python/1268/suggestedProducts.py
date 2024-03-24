class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        l = 0
        r = len(products) - 1
        for i in range(len(searchWord)):
            c = searchWord[i]
            res.append([])
            while l <= r and (len(products[l]) <= i or c != products[l][i]):
                l += 1
            while l <= r and (len(products[r]) <= i or c != products[r][i]):
                r -= 1
            for j in range(l, l + (min(3, r -l + 1))):
                res[-1].append(products[j])
        return res
