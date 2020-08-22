def findPairs(nums, k):
    hash_map = {}

    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1

    count = 0

    for key in hash_map:
        if k > 0 and key + k in hash_map:
            count += 1
        if k == 0 and hash_map[key] > 1:
            count += 1

    return count
