def characterReplacement(s: str, k: int) -> int:
    count = {}
    max_freq = 0
    l = 0
    result = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        max_freq = max(max_freq, count[s[r]])

        while (r - l + 1) - max_freq > k:
            count[s[l]] -= 1
            l += 1

        result = max(result, r - l + 1)

    return result


# Test cases
print(characterReplacement("ABAB", 2))    # Expected: 4
print(characterReplacement("AABABBA", 1)) # Expected: 4
print(characterReplacement("AAAA", 0))    # Expected: 4
print(characterReplacement("ABCDE", 1))   # Expected: 2