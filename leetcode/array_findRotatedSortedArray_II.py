# Here the difference from findRotatedSorted Array problem is that
# the array can contain duplicates
# hence we consider on additional specific condition

# Time: O(log N) -  Binary search
# Space: O(1)


def findRotatedSorted(nums, target):
    if len(nums) == 0:
        return False

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + (high - low)) // 2

        if target == nums[mid]:
            return True

        # this is the additional condition which keeps on incrementing the
        # low pointer when nums[low] value is equal to nums[mid] so
        # that the algo does not get stuck among those duplicates
        while low < mid and nums[low] == nums[mid]:
            low += 1

        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False
