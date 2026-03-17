# Leetcode: https://leetcode.com/problems/merge-intervals/
# Youtube: https://www.youtube.com/watch?v=44H3cEC2fFM

intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort(key = lambda i: i[0])
output = [intervals[0]]

for start, end in intervals[1:]:
    lastOutput = output[-1][1]

    if lastOutput >= start:
        output[-1][1] = max(end, lastOutput)
    else:
        output.append([start, end])

print(output)