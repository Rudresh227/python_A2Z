import math

def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)
    result = right

    while left <= right:
        k = (left + right) // 2
        hours = 0

        for p in piles:
            hours += math.ceil(p / k)

        if hours <= h:
            result = min(result, k)
            right = k - 1
        else:
            left = k + 1

    return result


print(minEatingSpeed([3, 6, 7, 11], 8))   # 4
print(minEatingSpeed([30, 11, 23, 4, 20], 5))  # 30
print(minEatingSpeed([30, 11, 23, 4, 20], 6))  # 23
print(minEatingSpeed([1000000000], 2))     # 500000000