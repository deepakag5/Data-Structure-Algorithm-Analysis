def maxProductSubArray(nums):
    # base case
    if len(nums) == 0:
        return []

    maxprod, minprod, best = 1, 1, nums[0]

    for num in nums:
        if num < 0:
            maxprod, minprod = minprod, maxprod

        maxprod = max(maxprod * num, num)
        minprod = min(minprod * num, num)

        best = max(best, maxprod)

    return best


def maxProductSubArray1(nums):
    # base case
    if len(nums) == 0:
        return []

    maxprod, minprod, best = 1, 1, nums[0]

    for num in nums:
        maxprod, minprod = max(maxprod * num, minprod * num, num), min(minprod * num, maxprod * num, num)

        best = max(maxprod, best)

    return best


def maxProductSubArray2(nums):
    # base case
    if len(nums) == 0:
        return []

    rev_num = nums[::-1]

    for i in range(1, len(nums)):
        nums[i] *= nums[i - 1] or 1
        rev_num[i] *= rev_num[i - 1] or 1

    return max(nums + rev_num)


print(maxProductSubArray2([2, 3, -2, 4]))
