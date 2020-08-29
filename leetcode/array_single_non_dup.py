# Time : O(log n)
# Space: O(1)


def single_non_dup(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        halves_are_even = (high - mid) % 2 == 0
        if nums[mid] == nums[mid + 1]:
            if halves_are_even:
                low = mid + 2
            else:
                high = mid - 1
        elif nums[mid] == nums[mid - 1]:
            if halves_are_even:
                high = mid - 2
            else:
                low = mid + 1
        else:
            return nums[mid]

    return nums[low]
