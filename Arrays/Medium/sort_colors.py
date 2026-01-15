"""
Problem: Sort Colors (Dutch National Flag Problem)

Given an array arr containing only the values 0, 1, and 2,
sort the array in-place so that all 0s come first,
followed by all 1s, and then all 2s.

You must solve this problem without using any built-in sort function.
The solution should run in one pass (O(n) time)
and use constant extra space (O(1)).

Example:
Input:  arr = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]

This is also known as the Dutch National Flag problem.
"""

arr = [2,0,2,1,1]

low = 0
mid = 0
high = len(arr) - 1

while mid <= high:
    if arr[mid] == 0:
        arr[mid],arr[low] = arr[low],arr[mid]
        mid += 1
        low += 1

    elif arr[mid] == 1:
        mid += 1

    else:
        arr[mid], arr[high] = arr[high],arr[mid]
        high -= 1

print(arr)
