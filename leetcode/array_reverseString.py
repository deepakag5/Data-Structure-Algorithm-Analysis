# Time: O(N)
# Space: O(1)
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        # swap
        s[left], s[right] = s[right], s[left]
        # increment pointers
        left, right = left + 1, right - 1
