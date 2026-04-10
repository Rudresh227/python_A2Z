def carFleet(target, position, speed):
    pairs = sorted(zip(position, speed), reverse=True)
    stack = []

    for pos, spd in pairs:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)

    return len(stack)


print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # 3
print(carFleet(10, [3], [3]))                             # 1
print(carFleet(100, [0, 2, 4], [4, 2, 1]))               # 1
print(carFleet(10, [6, 8], [3, 2]))                       # 2