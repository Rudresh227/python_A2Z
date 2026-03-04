a = [1, 2, 4, 4, 4, 5, 6]
b = [2, 3, 5, 7]

result = []
i,j = 0,0

while i < len(a) and j < len(b):
    if len(result) > 0 and result[-1] == a[i]:
        i += 1
        continue

    if len(result) > 0 and result[-1] == b[j]:
        j += 1
        continue

    if a[i] < b[j]:
        result.append(a[i])
        i += 1

    elif a[i] > b[j]:
        result.append(b[j])
        j += 1

    else:
        result.append(a[i])
        i += 1
        j += 1

while i < len(a):
    result.append(a[i])
    i += 1

while j < len(b):
    result.append(b[j])
    j += 1

print(result)