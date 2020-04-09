# Approach  1: this problem can also be done using - sorted(nums)[-k] - O(N log N), O(1)
# Approach 2: or using extra space heap - heapq.nlargest(k, nums)[-1] - O(N log k), O(N)


# Approach 3: using QuickSelect
# Time : O(N)    - O(N^2) worst case
# Space : O(1)

# O(1) space due to tail recursion. Tail recursion means the last thing this function is going to do is to return itself.
# System will pop up the current function from stack and put a new one into stack.

# Similar to quicksort algo wr choose a pivot and place elements to its either side.
# In quicksort we recursively check for the both parts that would result in O(N logN) time complexity.
# Here there is no need to deal with both parts since now one knows in which part to search for
# N - kth smallest element, and that reduces average time complexity to O(N)

import random


def findKthLargest(nums, k):
    """
    :param nums: List
    :param k: int
    :return: int
    """

    def partition(left, right, pivot_index):
        # get the pivot element
        pivot = nums[pivot_index]
        # swap the pivot with rightmost element
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        # get the starting index to iterate
        # and reach the actual position when sorted as per pivot
        j = left

        # iterate over the array to shift smaller elements to the left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        # move the pivot to its final place
        nums[j], nums[right] = nums[right], nums[j]

        return j

    def select(left, right, k_smallest):
        # if left and right both are 0 means there's only one element
        if left == right:
            return nums[left]

        # get a random index for pivot
        pivot_index = random.randint(left, right)

        # get pivot index as it would be in a sorted array by using partition
        pivot_index_sorted = partition(left, right, pivot_index)

        # if index we are looking for (k_smallest) matches pivot index matches return it
        # if k_smallest is less than pivot index then our item lies in left sub-array keep doing recursion
        # otherwise item lies in right sub-array keep doing recursion to right of pivot till end
        if k_smallest == pivot_index_sorted:
            return nums[k_smallest]
        elif k_smallest < pivot_index_sorted:
            return select(left, pivot_index_sorted - 1, k_smallest)
        else:
            return select(pivot_index_sorted + 1, right, k_smallest)

    return select(0, len(nums) - 1, len(nums) - k)
