# backtracking solution

def canPartitionKSubsetsSum(nums, k):
    # base case if list is empty or
    # if list cannot be divided in k equal int value buckets
    if not nums or sum(nums) % k != 0:
        return False

    # a list to keep track of values used
    used_nums = [None] * len(nums)

    # recursively call functions with default values
    return canPartition(0, nums, used_nums, k, 0, sum(nums) / k)


def canPartition(start, nums, used_nums, k, inProgressSum, targetBucketSum):
    # when we have found k-1 bucket whatever bucket (1) left we can return
    if k == 1:
        return True

    # if we hit the required sum for the bucket
    # recurse for next bucket by decreasing the value of k
    if inProgressSum == targetBucketSum:
        return canPartition(0, nums, used_nums, k - 1, 0, targetBucketSum)

    # iterate over the values of list which have not been used till now
    for i in range(start, len(nums)):
        if not used_nums[i]:
            # make the value as used
            used_nums[i] = True
            # iterate to the next value by adding the sum to inProgress bucket
            if canPartition(i + 1, nums, used_nums, k, inProgressSum + nums[i], targetBucketSum):
                return True
            # if above conditions are not met then make value unused again
            used_nums[i] = False

    # if none of the above conditions gets satisfied
    # then given list cannot be divided into K equal sum partitions
    # hence return false
    return False
