def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    need = {}
    window = {}

    for c in s1:
        need[c] = need.get(c, 0) + 1

    l = 0
    for r in range(len(s2)):
        c = s2[r]
        window[c] = window.get(c, 0) + 1    

        # Shrink window once it exceeds s1's length
        if r - l + 1 > len(s1):
            left = s2[l]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            l += 1

        if window == need:
            return True

    return False

# Tests
print(checkInclusion("ab", "eidbaooo"))  # True
print(checkInclusion("ab", "eidboaoo"))  # False
print(checkInclusion("adc", "dcda"))     # True