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


# search by constructing subset sums

def canPartitionKSubsets(nums, k):
    target = int(sum(nums) / k)

    # if reminder is not zero then cannot divide in equal int buckets
    if sum(nums) % k != 0:
        return False

    def search(groups):
        # base case if list is empty
        if not nums:
            return True
        # get the last number (highest as we have sorted) in the list
        v = nums.pop()

        # iterate for each bucket (value in the bucket list)
        for i, group in enumerate(groups):
            # if value in the bucket is less than the target then add the last value
            if group + v <= target:
                groups[i] += v
                # if we have successfully filled the buckets
                if search(groups):
                    return True
                groups[i] -= v
            if not group:
                break

        return False

    # sort the list
    nums.sort()
    # if the largest num in list is greater than target then
    # list cannot be divided in K equal sum buckets
    if nums[-1] > target:
        return False
    # if any of the num matches the target then it
    # should be alone in the bucket (assuming no zeroes)
    # remove the number from the list and also the number of buckets
    while nums and nums[-1] == target:
        nums.pop()
        k -= 1

    # we have passed a list of K-1 buckets with zero value
    return search([0] * k)
