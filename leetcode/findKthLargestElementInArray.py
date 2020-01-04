import random


def findKthLargest(nums, k):
    def partition(left, right, pivot_index):

        pivot = nums[pivot_index]

        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        j = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        nums[j], nums[right] = nums[right], nums[j]

        return j

    def select(left, right, k_smallest):
        if left == right:
            return nums[left]

        pivot_index = random.randint(left, right)

        pivot_index_sorted = partition(left, right, pivot_index)

        if k_smallest == pivot_index_sorted:
            return nums[k_smallest]
        elif k_smallest < pivot_index_sorted:
            return select(left, pivot_index_sorted - 1, k_smallest)
        else:
            return select(pivot_index_sorted - 1, right, k_smallest)

    return select(0, len(nums) - 1, len(nums) - k)


print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
