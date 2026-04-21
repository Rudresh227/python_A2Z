class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = [0] * (len(nums1) + len(nums2))

        i = j = k = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1
            k += 1

        while i < len(nums1):
            nums[k] = nums1[i]
            i += 1
            k += 1

        while j < len(nums2):
            nums[k] = nums2[j]
            j += 1
            k += 1

        n = len(nums)
        mid = n // 2
        if n % 2 == 1:
            return float(nums[mid])
        else:
            return (nums[mid - 1] + nums[mid]) / 2.0


# Tests
sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))           # 2.0
print(sol.findMedianSortedArrays([1, 2], [3, 4]))         # 2.5
print(sol.findMedianSortedArrays([], [1]))                # 1.0
print(sol.findMedianSortedArrays([1, 3, 5], [2, 4, 6]))  # 3.5