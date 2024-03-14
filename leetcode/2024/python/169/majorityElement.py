class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        freq = 1
        for i in range(1, len(nums)):
            if nums[i] == maj:
                freq += 1
            else:
                freq -= 1
            if freq == 0:
                maj = nums[i]
                freq = 1
        return maj
