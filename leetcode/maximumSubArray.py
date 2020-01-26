def maxSubArrayGreedy(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums

    curr_sum = max_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum


def maxSubArrayDP(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums

    max_sum = nums[0]

    for i in range(1, len(nums)):
        # print(nums[i-1])
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]

        max_sum = max(max_sum, nums[i])

    return max_sum


def maxSubArrayGreedy_returnarray(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums

    curr_sum = max_sum = nums[0]

    start = [0]
    end = [0]
    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])

        if curr_sum < 0:
            start[0] = i + 1

        if max_sum < curr_sum:
            end[0] = i

        max_sum = max(max_sum, curr_sum)

    print("start: " + str(start[0]))
    print("end: " + str(end[0]))

    return max_sum, nums[start[0]:end[0] + 1]


def maxSubArrayDP_returnarray(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums

    # make a copy of nums to return the max sum subarray later
    nums_copy = nums[:]

    max_sum = nums[0]

    start = [0]
    end = [0]

    for i in range(1, len(nums)):
        # print(nums[i-1])
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]

        if nums[i] < 0:
            start[0] = i + 1

        if max_sum < nums[i]:
            end[0] = i

        max_sum = max(max_sum, nums[i])

    return max_sum, nums_copy[start[0]:end[0] + 1]
