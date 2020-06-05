# Time: O(N)
# Space: O(1)

def rotate(nums, k):
    idx_to_rotate_from = len(nums) - k

    # nums = nums[:idx_to_rotate_from]+nums[idx_to_rotate_from:]
    x1 = nums[:idx_to_rotate_from]
    x2 = nums[idx_to_rotate_from:]
    nums = x2 + x1
    return nums


def rotate_usingswap(nums, k):
    def swap(nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    k %= len(nums)
    swap(nums, 0, len(nums) - 1)
    swap(nums, 0, k - 1)
    swap(nums, k, len(nums) - 1)
