# Time: O(n^2)
# Space: O(n)


def threeSum(nums, target):
    # base case
    if len(nums) <= 2:
        return [-1, -1]

    # as the best conceivable runtime (BCR) is O(n^2)
    # sorting (O(n log n) doesn't make it worse and will help
    nums.sort()
    result = []

    for i in range(len(nums)):
        # as we need nums to sum up to zero
        # and we have sorted the numbers even
        # if the current value is greater than zero,
        # break from the loop. Remaining values cannot sum to zero.
        if nums[i] > 0:
            break
        # if the current value is the same as the one before, skip it.
        if i == 0 or (nums[i - 1] != nums[i]):
            twoSum_II(nums, i, result)

    return result


def twoSum_II(nums, i, result):
    # select low pointer to i+1 (remember we want sum of
    # three num at index i, low, high!)
    low, high = i + 1, len(nums) - 1

    while low < high:
        sum_nums = nums[i] + nums[low] + nums[high]

        # if the sum of nums[i], nums[lo] and nums[hi] is less than zero, increment lo.
        # also increment lo if the value is the same as for lo - 1 (skip duplicates)
        if sum_nums < 0 or (low > i + 1 and nums[low] == nums[low - 1]):
            low += 1
        # if the sum of nums[i], nums[lo] and nums[hi] is greater than zero, decrease high.
        # also decrease high if the value is the same as for high+1
        elif sum_nums > 0 or (high < len(nums) - 1 and nums[high] == nums[high + 1]):
            high -= 1
        # otherwise, we found a triplet:
        # add it to the result res.
        # decrement high and increment low
        else:
            result.append([nums[i], nums[low], nums[high]])
            low += 1
            high -= 1
