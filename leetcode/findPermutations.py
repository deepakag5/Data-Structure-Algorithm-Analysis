# Time: O(NxN!) - for each k (each first) one performs N(N - 1) ... (N - k + 1)N(N−1)...(N−k+1) operations,
# and k is going through the range of values from 1 to N (and first from 0 to N - 1)
# Space : O(NXN!) since one has to keep N! solutions (N is for temp list)

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


# Backtracking Solution
# Time: O(NxN!) - for each k (each first) one performs N(N - 1) ... (N - k + 1)N(N−1)...(N−k+1) operations,
# and k is going through the range of values from 1 to N (and first from 0 to N - 1)
# Space : O(N!) since one has to keep N! sol

def permutations_SpaceOptimized(nums):
    def backtrack(first=0):
        # if all integers are used up
        if first == n:
            output.append(nums[:])
            print(output)
        for i in range(first, n):
            # place ith integer after current permutation
            nums[first], nums[i] = nums[i], nums[first]
            # use next integers to complete the permutation
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    output = []
    backtrack()
    return output
