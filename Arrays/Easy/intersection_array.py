from pandas.core.computation.expr import intersection

arr1 = [1, 2, 4, 4, 4, 5, 6]
arr2 = [2, 3, 5, 7]

intersection = []
i = j = 0

while i < len(arr1) and j < len(arr2):
    if len(intersection) > 0 and arr1[i] == arr1[i - 1]:
        i += 1
        continue

    if len(intersection) > 0 and arr2[j] == arr2[j - 1]:
        j += 1
        continue

    if arr1[i] > arr2[j]:
        j += 1

    elif arr1[i] < arr2[j]:
        i += 1

    else:
        intersection.append(arr1[i])
        i += 1
        j += 1

if i < len(arr1):
    intersection.append(arr1[i])
    i += 1

if i < len(arr2):
    intersection.append(arr2[j])
    j += 1

print(intersection)

