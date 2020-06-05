# Time: O(N)
# Space: O(2k)

def removeMinToMakeAanagram(s, t):
    # make hash array for both string
    # and calculate
    # frequency of each character
    count1 = [0] * 26
    count2 = [0] * 26

    # count frequency of each character
    # in first string
    i = 0
    while i < len(s):
        count1[ord(s[i]) - ord('a')] += 1
        i += 1

    # count frequency of each character
    # in second string
    j = 0
    while j < len(t):
        count2[ord(s[j]) - ord('a')] += 1
        j += 1

    # traverse count arrays to find
    # number of characters
    # to be removed
    result = 0
    for i in range(len(count1)):
        result += abs(count1[i] - count2[i])

    return result


# Time: O(N)
# Space: O(k)


def removeMinToMakeAanagramOpt(s, t):
    count1 = [0] * 26

    for char in s:
        count1[ord(char) - ord('a')] += 1

    for char in t:
        count1[ord(char) - ord('a')] -= 1

    return sum(map(abs, count1))
