def dailyTemperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  # stores indices

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)

    return result


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1, 1, 4, 2, 1, 1, 0, 0]
print(dailyTemperatures([30, 40, 50, 60]))                   # [1, 1, 1, 0]
print(dailyTemperatures([30, 60, 90]))                       # [1, 1, 0]
print(dailyTemperatures([90, 80, 70, 60]))                   # [0, 0, 0, 0]