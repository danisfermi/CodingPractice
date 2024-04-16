class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        pre = [0] * (n+1)
        pos = [0] * (n+1)
        res = 0
        for i in range(1, n+1):
            if customers[i-1] == "N":
                pre[i] = pre[i-1] + 1
            else:
                pre[i] = pre[i-1]
        for i in range(n-1, -1, -1):
            if customers[i] == "Y":
                pos[i] = pos[i+1] + 1
            else:
                pos[i] = pos[i+1]
        pen = float("inf")
        for i in range(n+1):
            if pre[i] + pos[i] < pen:
                pen = pre[i] + pos[i]
                res = i
        return res
