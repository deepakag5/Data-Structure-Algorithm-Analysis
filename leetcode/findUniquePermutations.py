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



def permsbacktrack_II(nums):
    def backtrack(temp_list, first=0):
        if len(temp_list) == len(nums):
            output.append(temp_list)
            return

        used = {}
        for i in range(first, n):
            if nums[i] in used:
                continue
            used[nums[i]] = True
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(temp_list + [nums[first]], first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    output = []
    backtrack([])
    return output
