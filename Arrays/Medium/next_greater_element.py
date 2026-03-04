from typing import List

def next_greater_element(arr: List[int]) -> List[int]:
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n):

        # If current element is greater than stack top
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]

        stack.append(i)

    return result


arr = [4, 5, 2, 10, 8]
print(next_greater_element(arr))