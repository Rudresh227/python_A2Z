# Leetcode: https://leetcode.com/problems/merge-sorted-array/description/

#Brute Force

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
result = []

i, j = 0, 0

while i < m and j < n:
    if nums1[i] < nums2[j]:
        result.append(nums1[i])
        i += 1

    elif nums1[i] > nums2[j]:
        result.append(nums1[i])
        j += 1

    else:
        result.append(nums1[i])
        result.append(nums2[j])
        i += 1
        j += 1

while i < m:
    result.append(nums1[i])
    i += 1

while j < n:
    result.append(nums2[j])
    j += 1

print(result)

#Optimal
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

last_idx = m + n - 1

while m > 0 and n > 0:
    if nums1[m - 1] > nums2[n - 1]:
        nums1[last_idx] = nums1[m - 1]
        m -= 1
    else:
        nums1[last_idx] = nums2[n - 1]
        n -= 1
    last_idx -= 1
while n > 0:
    nums1[last_idx] = nums2[n - 1]
    n -= 1

print(nums1)
