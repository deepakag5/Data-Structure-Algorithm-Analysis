# Time: O(N)
# Space: O(N)

# here the difference from valid palindrome is that we can remove one char and check if it's
# palindrome or not

def validPalin(s):
    # edge case
    # because if it's empty string or one char it'll be a palindrome
    # also when there are two chars, we can delete one char and it'll again be a palindrome !
    if len(s) <= 2:
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # when there is a mismatch take one string with all the chars except the right char [left:right]
            # and another string with all chars except left char (left+1)
            left_str, right_str = s[left:right], s[left + 1:right + 1]
            # now as we are allowed only one char mismatch if the rest of the string
            # match with its reverse (the very definition of a palindrome !!) then it's a
            # palindrome else not
            return left_str == left_str[::-1] or right_str == right_str[::-1]
        left, right = left + 1, right - 1

    return True
