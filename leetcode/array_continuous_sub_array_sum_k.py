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


# Optimized using hashmap
# Time: O(n)
# Space: O(min(n,k))

def conSubArraySumK_hm(nums, k):
    if len(nums) == 0:
        return False

    if len(nums) == 1 and nums[0] % k != 0:
        return False

    # to store the remainder of sum at location - i
    presum = {}
    presum[0] = -1
    sum_val = 0

    for i, num in enumerate(nums):
        sum_val += num

        if k != 0:
            sum_val = sum_val % k

        # if the remainder has been seen before
        # then both the numbers are in same group
        # if the results of two integers i1 and i2 modulo k are the same, then we can say they are in the same group
        # e.g. 7 % 13 = 7 and 46 % 13 = 7, so we can think of 7 and 46 are in the same group
        # we can name the group using the result of modulo
        # if we know two integers i1 and i2 are in the same group d, then we have:
        # i1 = 13 * a + d and i2 = 13 * b + d where a and b are both integers
        # if then we calculate their difference, we can get:
        # i1 - i2 = 13 * a - 13 * b + d - d = 13 * (a - b)
        if sum_val in presum:
            if i - presum[sum_val] >= 2:
                return True
        else:
            presum[sum_val] = i

    return False
