from typing import List

def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1  # search left half
        else:
            left = mid + 1   # search right half

    return -1  # not found

arr = [1,3,5,7,9]
target = 5

