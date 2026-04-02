from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    result = []
    dq = deque()
    l = r = 0

    while r < len(nums):
        while dq and nums[dq[-1]] < nums[r]:
            dq.pop()

        dq.append(r)

        while dq and dq[0] < l:
            dq.popleft()

        if r + 1 >= k:
            result.append(nums[dq[0]])
            l += 1
        r += 1

    return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(maxSlidingWindow(nums, k))