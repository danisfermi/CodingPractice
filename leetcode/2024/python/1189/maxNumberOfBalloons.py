class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = "balloon"
        hm = {}
        for ele in text:
            if ele in ans and ele not in hm:
                hm[ele] = 1
            elif(ele in ans):
                hm[ele] += 1
        ballon = {
            "b":1,
            "a":1,
            "l":2,
            "o":2,
            "n":1
        }
        count = 0
        while True:
            for key, value in ballon.items():
                if key in hm and hm[key] >= ballon[key]:
                    hm[key] -= ballon[key]
                else:
                    return count
            count+=1

        return count
