def maxProductSubArray(nums):
    maxprod, minprod, best = 1, 1, nums[0]

    for num in nums:
        if num < 0:
            maxprod, minprod = minprod, maxprod

        maxprod = max(maxprod * num, num)
        minprod = min(minprod * num, num)

        best = max(best, maxprod)

    return best
