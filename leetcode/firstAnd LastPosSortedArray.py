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
