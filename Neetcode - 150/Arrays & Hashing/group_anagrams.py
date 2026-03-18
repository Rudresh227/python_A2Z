def groupAnagrams(strs):
    groups = {}

    for s in strs:
        key = ''.join(sorted(s))   # sort to get the canonical key
        if key not in groups:
            groups[key] = []
        groups[key].append(s)      # group original string under its key

    print('Groups', groups)

    return list(groups.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))