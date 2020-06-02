# Time : O(l1+(l2-l1))
# Space : O(1)

def containsStrPerm(s1, s2):
    l1 = [0] * 26
    l2 = [0] * 26

    # ord(char) - ord('a') gives position of character in list
    # for ex. ord('b')-ord('a') would be 1 means l1[1] = 1
    for char in s1:
        l1[ord(char) - ord('a')] += 1

    # iterate over string 2
    for i in range(len(s2)):
        l2[ord(s2[i]) - ord('a')] += 1
        # for characters at length greater than string 1 decrease the count
        # the idea is whichever the characters encountered before we find
        # a continuous string permutation we need to decrease their count
        if i >= len(s1):
            l2[ord(s2[i - len(s1)]) - ord('a')] -= 1

        if l1 == l2:
            return True

    return False