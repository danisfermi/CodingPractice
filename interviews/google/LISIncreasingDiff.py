import functools
from bisect import bisect_left

nums = [1, 2, 4, 5, 7, 1, 5, 2, 6, 4, 1, 19]
A = sorted([num, idx] for idx, num in enumerate(nums))

@functools.lru_cache(None)
def dp(pre, cur):
    if cur >= len(A):
        return 0
    res = dp(pre, cur + 1)
    if A[cur][1] > A[pre][1]:
        dif = A[cur][0] - A[pre][0]
        
        new_idx = bisect_left(A, [dif + A[cur][0] + 1, float('-inf')])
        
        if new_idx > cur:
            res = max(res, 1 + dp(cur, new_idx))
    return res

# Call the dp function to get the result
res = max(1 + dp(a, b) for a in range(len(A)) for b in range(a + 1, len(A)))
print(res)

