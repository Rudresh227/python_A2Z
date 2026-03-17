# GFG: https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=inversion-of-array
# Youtube: https://www.youtube.com/watch?v=AseUmwVNaoY&t=152s

#Brute
nums = [5,3,2,4,1]
count = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            count += 1

print(count)

#Better - Two pointer+
nums1 = [2,3,5,6]
nums2 = [2,2,4,4,8]
i = 0
j = 0
count = 0
while i < len(nums1)  and j < len(nums2):
    if nums1[i] > nums2[j]:
        count += (len(nums1) - i)
        j += 1
    else:
        i += 1

print(f"Total Inversions: {count}")

#Optimal - Merge Sort
def merge_sort(arr):
    count = 0

    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        count += merge_sort(left_arr)
        count += merge_sort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                # left_arr[i] > right_arr[j]
                # All remaining elements in left_arr are greater than right_arr[j]
                arr[k] = right_arr[j]
                count += len(left_arr) - i
                j += 1

            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return count


arr = [5, 3, 2, 4, 1]
total_inversions = merge_sort(arr)

print(f"Sorted Array     : {arr}")
print(f"Total Inversions : {total_inversions}")

# ## How it works — Step by Step
# ```
# Original: [5, 3, 2, 4, 1]
#
#           [5, 3, 2, 4, 1]
#            /             \
#       [5, 3, 2]        [4, 1]
#        /     \          /   \
#     [5, 3]   [2]      [4]   [1]
#     /    \
#   [5]   [3]
#
# Merge [5] and [3]:
#   5 > 3 → count += 1  →  merged: [3, 5]     count = 1
#
# Merge [3, 5] and [2]:
#   3 > 2 → count += 2  →  merged: [2, 3, 5]  count = 3
#
# Merge [4] and [1]:
#   4 > 1 → count += 1  →  merged: [1, 4]     count = 4
#
# Merge [2, 3, 5] and [1, 4]:
#   2 > 1 → count += 3  →  merged: [1, ...]   count = 7
#   3 ≤ 4 →              →  merged: [1, 2, 3]
#   5 > 4 → count += 1  →  merged: [1, 2, 3, 4, 5]  count = 8
#
# Total Inversions: 8