# Time: O(log N) - binary search
# Space: O(1)

def findMin(nums):
    if len(nums) == 1:
        return nums[0]

    low = 0
    high = len(nums) - 1

    if nums[high] > nums[0]:
        return nums[0]

    while low <= high:
        mid = (low + high) // 2

        # if mid number is greater than following one -
        # we found inflection point retrun the mid+1 number
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        # if number before mid is greater than mid -
        # we found inflection point retrun the mid number
        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        # if number at mid still greater than the start of array
        # our min nuumber still lies somewhere on the right
        # hence advance left else decrease right
        if nums[mid] > nums[0]:
            low = mid + 1
        else:
            high = mid - 1
