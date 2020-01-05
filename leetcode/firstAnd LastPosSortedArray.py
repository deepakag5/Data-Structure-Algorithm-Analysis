# O(n) solution

def searchRange(nums, target):
    if not nums:
        return [-1, -1]

    for i in range(len(nums)):
        if nums[i] == target:
            left_index = i
            break
        else:
            return [-1, -1]

    for j in range(len(nums) - 1, -1, -1):
        if nums[j] == target:
            right_index = j
            break

    return [left_index, right_index]


# O(log n) solution

def searchRangeOptimized(nums, target):
    if not nums:
        return [-1, -1]

    def search(n):
        low, high = 0, len(nums)

        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= n:
                high = mid
            else:
                low = mid + 1

        return low

    low = search(target)

    return [low, search(target + 1) - 1] if target in nums[low:low + 1] else [-1, -1]
