# Brute Force - O(n^3)
# Check all the substring one by one to see if it has no duplicate character.


def lengthOflongest_substr_brute(s):
    for i in range(len(s)):  # O(n)
        for j in range(i + 1, len(s)):  # O(n^2)
            if allUnique(s, i, j):  # O(n^3)
                ans = max(ans, j - i)
    return ans


def allUnique(s, start, end):
    hash_set = set()
    for i in range(start, end):
        if s[i] in hash_set:
            return False
            hash_set.add(s[i])
    return true


# Time: O(2N)  we are traversing the list with two i,j
# Space: O(min(m,n))  size of unique chars in set


# We use HashSet to store the characters in current window [i, j)[i,j) (j = ij=i initially).
# Then we slide the index j to the right. If it is not in the HashSet, we slide j further.
# Doing so until s[j] is already in the HashSet. At this point
# we found the maximum size of substrings without duplicate characters start with index i.
# If we do this for all i, we get our answer.
def lengthOflongest_substr(s):
    n = len(s)
    hash_set = set()
    ans, i, j = 0, 0, 0
    while i < n and j < n:
        if s[j] not in hash_set:
            hash_set.add(s[j])
            j += 1
            ans = max(ans, j - i)
        else:
            hash_set.remove(s[i])
            i += 1
    return ans


# sliding window optimized using hash map
# Time: O(N)  we are traversing the list
# Space: O(1)  we have 26 chars else O(N)

def lengthOflongest_hashmap(s):
    n = len(s)
    hash_map = {}
    ans, i, j = 0, 0, 0
    for j in range(n):
        if s[j] in hash_map:
            i = max(hash_map.get(s[j]), i)
        ans = max(ans, j - i + 1)
        hash_map[s[j]] = j + 1
    return ans


# More optimized hash_map version
def lengthOflongest(s):
    if len(s) == 0:
        return 0

    start = 0
    maxlength = 0
    hash_tbl = {}

    for i in range(len(s)):
        # to keep track of repeating character
        # if the character is in hash_tbl and also it start pointer is less than
        # index of repeating character even before current repeating character
        # for example for string abcdbac it will skip the second a as start pointer is
        # currently at first b (start=1 and index of first a is 0) hence this loop should get skipped
        if s[i] in hash_tbl and start <= hash_tbl[s[i]]:
            start = hash_tbl[s[i]] + 1
        else:
            maxlength = max(maxlength, i - start + 1)
        hash_tbl[s[i]] = i

    return maxlength
