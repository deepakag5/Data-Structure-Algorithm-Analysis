# Time: O(N)
# Space: O(1)

# Given - [1,3,5,4,7]
# Expected Result - 3 - (longest cont incr subseq = [1,3,5])

def lenOfContinuousIncrSub(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1

    maxlen = 1
    count = 1

    for i in range(len(nums) - 1):
        # keep increasing counter
        # when next element is greater than prev element
        if nums[i] < nums[i + 1]:
            count += 1
        else:
            # reset the counter once we have reached a number
            # which is smaller than prev
            count = 1

        maxlen = max(maxlen, count)

    return maxlen
