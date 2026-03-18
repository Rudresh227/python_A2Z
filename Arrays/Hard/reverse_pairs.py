def reversePairs(arr):
    count = 0

    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        count += reversePairs(left_arr)
        count += reversePairs(right_arr)

        j = 0
        for i in range(len(left_arr)):
            while j < len(right_arr) and left_arr[i] > 2 * right_arr[j]:
                j += 1
            count += j

        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
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





arr = [1,3,2,3,1]
total_inversions = reversePairs(arr)

print(f"Sorted Array     : {arr}")
print(f"Total Reverse Pairs : {total_inversions}")