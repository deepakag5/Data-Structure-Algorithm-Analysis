def permute(nums):
    permutations = [[]]

    for num in nums:
        new_perms = []
        for perm in permutations:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [num] + perm[i:])
        permutations = new_perms

    return permutations

print(permute([1,2,3]))

