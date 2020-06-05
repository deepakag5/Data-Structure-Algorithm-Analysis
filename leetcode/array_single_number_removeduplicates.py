# Time: O(N^2)
# Space: O(N)

def singleNumber(nums):
    list_dedup = []
    for i in nums:  # this takes O(N)
        if i not in list_dedup:
            list_dedup.append(i)
        else:
            list_dedup.remove(i)  # this takes O(N)

    return list_dedup.pop()


# Time: O(N)
# Space: O(N)
def singleNumber_hash(nums):
    hash_table = {}

    for i in nums:
        try:
            hash_table.pop(i)
        except:
            hash_table[i] = 1

    return hash_table.popitem()[0]


# Time: O(N)
# Space: O(1)
def singleNumber_XOR(nums):
    a = 0
    for i in nums:
        a ^= i

    return a
