def encode(strs):
    result = ""
    for s in strs:
        result += (str(len(s)) + "#" + s)
    return result

def decode(s):
    result = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1

        length = int(s[i : j])
        result.append(s[j + 1: j + 1 + length])
        i = j + 1 + length


    return result


# Test
strs = ["neet", "co#de", "lo ve"]
encoded = encode(strs)
print(encoded)          # "4#neet5#co#de5#lo ve"
print(decode(encoded))  # ["neet", "co#de", "lo ve"]