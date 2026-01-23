def rearrange(nums):
    pos = 0
    neg = 1

    result = [0]* len(nums)

    for num in nums:
        if num > 0:
            result[pos] = num
            pos += 2

        else:
            result[neg] = num
            neg += 2

    return result


nums = [3,1,-2,-5,2,-4]
print(rearrange(nums))

