def permuteUniqueIterative(nums):
    if len(nums)<1:
        return [[]]

    permutations = [[]]

    for num in nums:
        new_perms = []

        for perm in permutations:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i]+[num]+perm[i:])
                # to avoid duplicates if i val is less than len of prem and perm val is equal to curent num
                if i<len(perm) and perm[i]==num:
                    break

        permutations = new_perms

    return permutations