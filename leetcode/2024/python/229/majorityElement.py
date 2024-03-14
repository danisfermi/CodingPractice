class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
            if len(count) <= 2:
                continue
            newCount = defaultdict(int)
            for i, j in count.items():
                if j > 1:
                    newCount[i] = j - 1
            count = newCount
        res = []
        for i in count:
            if nums.count(i) > len(nums)//3:
                res.append(i)
        return res
