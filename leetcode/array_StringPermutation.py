# O(n^2)
# O(1)

def checkPermutation(s1, s2):
    # remove white spaces
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if len(s1) != len(s2):
        return False

    for char in s1:  # O(n)
        if char in s2:  # O(n)
            s2 = s2.replace(char, "")

    return len(s1) == len(s2)


# O(N log N) -- sorting
# O(1)

def checkPermutation_1(s1, s2):
    # remove white spaces
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if len(s1) != len(s2):
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


# O(N)
# O(N)   # extra space for hashmap

def checkPermutation_hashmap(s1, s2):
    # remove white spaces
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if len(s1) != len(s2):
        return False

    hashmap = {}

    for i in range(len(s1)):  # O(N)
        hashmap[s1[i]] = hashmap(s1[i], 0) + 1

    for char in s2:  # O(N)
        if char in hashmap:  # O(1)
            hashmap[char] -= 1
        if hashmap[char] < 0:  # O(1)
            print(hashmap)
            return False

    return True
