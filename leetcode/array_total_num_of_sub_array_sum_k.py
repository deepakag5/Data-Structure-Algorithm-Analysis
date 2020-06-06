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

        # if the cumulative sum upto two indices, say i and j is at a difference of k i.e. if sum[i] - sum[j] = k,
        # the sum of elements lying between indices i and j is k.
        # hashmap stores cumulative sum upto all the indices possible along with the number of times the
        # same sum occurs.
        if currSum - k in hashmap:
            count += hashmap[currSum - k]

        if currSum not in hashmap:
            hashmap[currSum] = 1
        else:
            hashmap[currSum] += 1

    # we have considered number k also as a sub-array if it's present in the array
    # for example - [3,4,7,2,-3,1,4,2] and k=7 will give
    # num of sub-array as 4 - [3,4], [7], [7,2,-3,1], [1,4,2]
    # but if we want our sub-arrays to have at least two items then
    # we can simply subtract the occurences of k in array

    # count_k = 0
    #
    # for num in nums:
    #     if num == k:
    #         count_k += 1
    #
    # count = count - count_k

    return count
