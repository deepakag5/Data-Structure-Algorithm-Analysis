# Time: O(n^2)
# Space: O(n)

def lenOflongestIncrSubSeq(nums):
    if len(nums) == 0:
        return 0

    dp = [1] * len(nums)
    maxlen = 1

    for i in range(len(dp)):
        maxval = 0
        j = 0
        while j < i:
            if nums[i] > nums[j]:
                maxval = max(maxval, dp[j])
            j += 1

        dp[i] = maxval + 1
        maxlen = max(maxlen, dp[i])

    return maxlen
