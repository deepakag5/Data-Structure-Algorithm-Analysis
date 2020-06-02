# Time: O(N)
# Space: O(2K) - used two hashmaps to store the chars

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    dict1, dict2 = {}, {}

    for item in s:
        dict1[item] = dict1.get(item, 0) + 1
    for item in t:
        dict2[item] = dict2.get(item, 0) + 1

    return dict1 == dict2


# Time: O(N)
# Space: O(K) - only one hashmap to store the chars

def isAnagramOpt(s, t):
    if len(s) != len(t):
        return False

    dict1 = {}

    for item in s:
        dict1[item] = dict1.get(item, 0) + 1

    for item in t:
        dict1[item] = dict1.get(item, 0) - 1

    for value in dict1.values():
        if value != 0:
            return False

    return True
