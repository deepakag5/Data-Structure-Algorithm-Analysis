def maxSubArrayGreedy(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums

    curr_sum = max_sum = nums[0]

    for i in range(len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum


def maxSubArrayDP(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums

    max_sum = nums[0]

    for i in range(len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
        max_sum = max(max_sum, nums[i])

    return max_sum


print(maxSubArrayDP([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
