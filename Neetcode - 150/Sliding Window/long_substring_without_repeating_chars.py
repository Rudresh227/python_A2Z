def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = 0
    maxlen = 0
    right = 0
    while right < len(s):
        if s[right] in char_index:
            left = max(left, char_index[s[right]] + 1)
        char_index[s[right]] = right
        maxlen = max(maxlen, right - left + 1)
        right += 1
    return maxlen

print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))     # 1
print(lengthOfLongestSubstring("pwwkew"))    # 3
print(lengthOfLongestSubstring(""))          # 0

