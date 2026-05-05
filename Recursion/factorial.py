def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# Test
print(factorial(5))  # 120


def add(n):
    if n == 0:
        return 1

    result = 1 if n > 1 else 0

    result += add(n - 1)

    return result

# Test
print(add(5))  # 120