def permuteIterative(nums):
    """
    :param nums: List
    :return: List[List]
    """
    # create a list of list to store results
    permutations = [[]]

    # iterate over all numbers
    for num in nums:
        # list to hold the temporary results
        new_perms = []

        # iterate over permutations
        for perms in permutations:
            # iterate over numbers in single permutation
            for i in range(len(perms)+1):
                new_perms.append(perms[:i]+[num]+perms[i:])
        # reassign temp results to permutations list
        permutations = new_perms

    return permutations


def permuteRecursive(nums):
    def rec_permute(nums):
        if len(nums)<1:
            return [[]]

        res_permutations = []

        for i in range(len(nums)):
            for perms in rec_permute(nums[:i]+nums[i+1:]):
                res_permutations.append([nums[i]]+perms)

        return res_permutations

    return rec_permute(nums)