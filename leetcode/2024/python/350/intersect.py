class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        res = []
        for n in nums1:
            m[n] = m.get(n, 0) + 1
        for n in nums2:
            if m.get(n, 0) > 0:
                res.append(n)
                m[n] -= 1
        return res
