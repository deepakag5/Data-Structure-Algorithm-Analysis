def maxSubArrayGreedy(nums):
    # base case - 1
    if not nums:
        return 0
    # base case - 2
    if len(nums) == 1:
        return nums

    curr_sum = max_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum


def maxSubArrayDP(nums):
    # base case - 1
    if not nums:
        return 0

    # base case - 2
    if len(nums) == 1:
        return nums

    max_sum = nums[0]

    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]

        max_sum = max(max_sum, nums[i])

    return max_sum


def maxSubArraySum_returnArray(nums):
    max_sum = float('-inf')
    curr_sum = 0
    # start = 0
    # end = 0
    # s = 0

    for i in range(0, len(nums)):

        curr_sum += nums[i]

        if max_sum < curr_sum:
            max_sum = curr_sum
            # we maintain the indices whenever we get max sum
            # start however gets replaced whenever we reset curr sum
            # start = s
            # end = i

        if curr_sum < 0:
            curr_sum = 0
            # s = i + 1

    return max_sum  # , nums[start:end+1]
