# Linear Search One Pass
# Time: O(N)
# Space: O(1)

def missingElement(nums, k):
    if len(nums):
        return 0

    def missing(idx):
        return nums[idx] - nums[0] - idx

    n = len(nums)

    if k > missing(n - 1):
        return nums[n - 1] + k - missing(n - 1)

    idx = 1

    while k > missing(idx):
        idx += 1

    return nums[idx - 1] + k - missing(idx - 1)


# Improvement - Making use of fact that array is sorted
# Binary Search
# Time: O(log N)
# Space: O(1)

def missingElementBinary(nums, k):
    if len(nums) == 0:
        return 0

    # Return how many numbers are missing until nums[idx]
    def missing(idx):
        return nums[idx] - nums[0] - idx

    n = len(nums)

    # If kth missing number is larger than
    # the last element of the array
    if k > missing(n - 1):
        return nums[n - 1] + k - missing(n - 1)

    left, right = 0, n - 1

    # find left = right index such that
    # missing(left - 1) < k <= missing(left)
    while left != right:
        pivot = (left + (right - left)) // 2

        if k > missing(pivot):
            left = pivot + 1
        else:
            right = pivot

    # kth missing number is greater than nums[left - 1]
    # and less than nums[left]
    return nums[left - 1] + k - missing(left - 1)
