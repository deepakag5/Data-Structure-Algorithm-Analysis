# Time: O(N)
# Space: O(1)


def firstMissingPos(nums):
    if 1 not in nums:
        return 1

    # as 1 is present (we already checked for not in)
    # and length of nums is one which means that number is 1
    # hence minimum pos number missing is 2
    if len(nums) == 1:
        return 2

    n = len(nums)

    # replace all zeros, negative and num greater than n as 1
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1

    # change to negative sign of numbers a at ath index
    for i in range(n):
        a = abs(nums[i])

        # as length of array is upto n-1 index
        # we change 0th index sign
        if a == n:
            nums[0] = - abs(nums[a])
        else:
            nums[a] = - abs(nums[a])

    # if any index other than zero has positive sign return that index
    # that will be first min pos
    for i in range(1, n):
        if nums[i] > 0:
            return i

    # if num at 0th index is greater than zero means number is n
    if nums[0] > 0:
        return n

    # if none of the above satisfies the number is n+1
    return n + 1
