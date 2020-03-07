# O(n), O(1) -- Using Division

def productExceptSelf_Division(nums):
    length = len(nums)

    product = 1

    for i in range(length):
        product *= nums[i]

    result = [0] * length

    for i in range(length):
        result[i] = int(product / nums[i])

    return result


# O(n), O(n) -- Without using division

def productExceptSelf(nums):
    length = len(nums)

    L, R, result = [0] * length, [0] * length, [0] * length

    L[0] = 1

    for i in range(1, length):
        L[i] = L[i - 1] * nums[i - 1]

    R[length - 1] = 1

    for i in reversed(range(length - 1)):
        R[i] = R[i + 1] * nums[i + 1]

    for i in range(length):
        result[i] = L[i] * R[i]
    return result


# O(n), O(1) -- Without using division and no extra space (return array is not considered as space)

def productExceptSelf_NoExtraSpace(nums):
    length = len(nums)

    result = [0] * length

    result[0] = 1

    for i in range(1, length):
        result[i] = result[i - 1] * nums[i - 1]

    R = 1

    for i in range(length):
        result[i] = result[i] * R
        R *= nums[i]

    return result
