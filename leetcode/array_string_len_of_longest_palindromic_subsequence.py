# Time: O(N^2)
# Space: O(1)

# Given - "babad"
# Expected Result - "bab" or "aba"


def longestAtIndex(s, l, r):
    # expand until the pointers reach the edges and characters are same
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    # move the pointers
    l += 1
    r -= 1

    return r - l + 1, l, r


def longestPalindromicSub(s):
    if not s:
        return ""

    maxlen = 0
    left = 0
    right = -1

    for i in range(len(s)):  # O(n)
        # need to perform for odd/even length palindrome
        # longestAtIndex(s,i,i)
        # longestAtIndex(s,i,i+1)
        for j in range(2):
            longest, l, r = longestAtIndex(s, i, i + j)  # O(n)
            if maxlen < longest:
                maxlen = longest
                left = l
                right = r

    return s[left:right + 1]
