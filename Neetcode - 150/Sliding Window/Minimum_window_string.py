def minWindow(s, t):
    if not t or not s:
        return ""

    need = {}
    for char in t:
        need[char] = need.get(char, 0) + 1

    have = {}

    formed = 0
    required = len(need)

    l = 0
    result = ""
    result_len = float("inf")

    for r in range(len(s)):
        char = s[r]
        have[char] = have.get(char, 0) + 1

        if char in need and have[char] == need[char]:
            formed += 1

        while formed == required:
            window_len = r - l + 1
            if window_len < result_len:
                result_len = window_len
                result = s[l:r+1]

            left_char = s[l]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1
            l += 1

    return result


print(minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
print(minWindow("ABC", "AAB"))            # ""
print(minWindow("a", "a"))               # "a"