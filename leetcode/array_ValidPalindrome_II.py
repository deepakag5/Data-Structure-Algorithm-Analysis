# Time: O(N)
# Space: O(N)

def validPalin(s):
    # edge case
    # because if it's empty string or one char it'll be a palindrome
    # also when there are two chars, we can delete one char and it'll again be a palindrome !
    if len(s) <= 2:
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            left_str, right_str = s[left:right], s[left + 1:right + 1]
            return left_str == left_str[::-1] or right_str == right_str[::-1]
        left, right = left + 1, right - 1

    return True