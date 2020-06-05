# Brute Force
# Time: O(n^2)
# Space: O(1)


def subArraySumK(nums, k):
    if len(nums) == 0:
        return 0

    count = 0

    for i in range(len(nums)):
        currSum = 0
        for j in range(i, len(nums)):
            currSum += nums[j]

            if currSum == k:
                count += 1

    return count


# Time: O(n)
# Space: O(n)

def subArraySumK1(nums, k):
    if len(nums) == 0:
        return 0

    hashmap = {0: 1}
    count, currSum = 0, 0

    for i in range(len(nums)):
        currSum += nums[i]

        if currSum - k in hashmap:
            count += hashmap[currSum - k]

        if currSum not in hashmap:
            hashmap[currSum] = 1
        else:
            hashmap[currSum] += 1

    return count
