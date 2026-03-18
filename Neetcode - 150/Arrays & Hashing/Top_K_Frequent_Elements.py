nums = [1,1,1,2,2,3]
k = 2

freq = {}
for num in nums:
    if num not in freq:
        freq[num] = 1
    else:
        freq[num] += 1

# Sort keys by frequency descending, take top k
sorted_keys = sorted(freq, key=lambda x: freq[x], reverse=True)
print(sorted_keys[:k])