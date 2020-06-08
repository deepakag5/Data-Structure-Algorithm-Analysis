# Time: O(n)
# Space: O(1)


def findAllAnagrams(s, p):
    # edge cases
    if len(s) == 0 or len(p) == 0:
        return []

    ns, np = len(s), len(p)

    if ns < np:
        return []

    s_count, p_count = [0] * 26, [0] * 26

    for char in np:
        p_count[ord(char) - ord('a')] += 1

    result = []

    # sliding window on the string s
    for i in range(ns):
        # add one more letter
        # on the right side of the window
        s_count[ord(s[i]) - ord('a')] += 1

        # remove one letter
        # from the left side of the window
        if i >= np:
            s_count[ord(s[i - np]) - ord('a')] -= 1

        # compare array in the sliding window
        # with the reference array
        if p_count == s_count:
            result.append(i + 1 - np)  # i+1-np as the array starts from 0

    # note if we want to return the actual anagrams
    # all we need to do is
    # result.append(s[(i+1-np):(i+1-np)+np])
    return result
