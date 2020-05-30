# Brute Force using cumulative sum
# Time: O(n^2)
# Space: O(n)


def conSubArraySumK(nums, k):
    if len(nums) == 0:
        return False

    if len(nums) == 1 and nums[0] % k != 0:
        return False

    sum_val = [0] * len(nums)
    sum_val[0] = nums[0]

    # get the cumulative sum
    for i in range(1, len(nums)):
        sum_val[i] = sum_val[i - 1] + nums[i]

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            temp_sum = sum_val[j] - sum_val[i] + nums[i]

        if temp_sum == k or (k != 0 and temp_sum % k == 0):
            return True

    return False
