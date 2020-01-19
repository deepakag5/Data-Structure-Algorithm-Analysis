# Here the difference from findMinRotatedSorted Array problem is that the array can contain duplicates
# hence we consider three specific conditions

# O(log N) - binary search algorithm. However, in the worst case where the array contains identical elements
# (i.e. case #3 nums[pivot]==nums[high]), the algorithm would deteriorate to iterating each element,
#  as a result, the time complexity becomes O(N).
# Space : O (1)


def findMin(nums):
    if len(nums) == 1:
        return nums[0]

    low = 0
    high = len(nums) - 1

    while low < high:
        pivot = low + (high - low) // 2  # to prevent integer overflow

        # case 1 the pivot lies to the right of rotation point
        if nums[pivot] < nums[high]:
            high = pivot
        # case 2 the pivot lies to the left of rotation point
        elif nums[pivot] > nums[high]:
            low = pivot + 1
        # case 3, nums[pivot]==nums[high]), reduce high value (not too aggressively)
        else:
            high = high - 1

    return nums[low]
