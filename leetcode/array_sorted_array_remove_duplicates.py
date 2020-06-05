# Time: O(N)
# Space: O(1)

def remove_Dup_Sorted(nums):
    # edge case empty array
    if len(nums) == 0:
        return 0

    i = 0

    for j in range(1, len(nums)):
        # if the array values are same then keep iterating(skip duplicates)
        if nums[i] == nums[j]:
            continue
        else:
            i += 1
            nums[i] = nums[j]

    return i + 1
