# backtraking solution

def canPartitionKSubsetsSum(nums, k):
    if not nums or sum(nums) % k != 0:
        return False

    used_nums = [None] * len(nums)

    return canPartition(0, nums, used_nums, k, 0, sum(nums) / k)


def canPartition(start, nums, used_nums, k, inProgressSum, targetBucketSum):
    if k == 1:
        return True

    if inProgressSum == targetBucketSum:
        return canPartition(0, nums, used_nums, k - 1, 0, targetBucketSum)

    for i in range(start, len(nums)):
        if not used_nums[i]:
            used_nums[i] = True
            if canPartition(i + 1, nums, used_nums, k, inProgressSum + nums[i], targetBucketSum):
                return True
            used_nums[i] = False

    return False


print(canPartitionKSubsetsSum([4, 3, 2, 3, 5, 2, 1], 4))
