def majorityElement(nums):
    hash_table = {}

    for num in nums:
        if num in hash_table.keys():
            hash_table[num] += 1
        else:
            hash_table[num] = 1

    max_value = 0

    for val in hash_table.values():
        if max_value < val:
            max_value = val

    # get key which has the maximum value
    return list(hash_table.keys())[list(hash_table.values()).index(max_value)]


from collections import Counter


def majorityElement_short(nums):
    count_elements = Counter(nums)
    # get key which has the maximum value
    return max(count_elements.keys(), key=count_elements.get)
