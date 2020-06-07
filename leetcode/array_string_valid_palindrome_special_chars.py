# Time: O(N)
# Space: O(N)

# here the difference from valid palindrome is that we can have space, special chars, uppercase chars


def validPalin(s):
    # let's remove the white spaces from string (if there are any)
    s = s.replace(" ", "")

    # note if the str can also contain \t and \n then to remove them we should use below
    # s = "".join(s.split())

    # now that we have removed white spaces it takes care of empty str case one/multiple spaces - " ", "  "

    # edge case
    # because if it's empty string or one char it'll be a palindrome
    # we are considering "$" also as valid palindrome
    if len(s) <= 1:
        return True

    i, j = 0, len(s) - 1

    while i < j:
        # compare the chars only if they both are alphabets
        # (remember we are treating digits as special chars and not using them for comparison
        # if we wish to consider digits as part of comparison then use isalnum() instead)
        if s[i].isalpha() and s[j].isalpha():
            # we are converting to lower as case sensitivity is not expected
            # if it's expected then remove lower
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        # if char at i is not alpha move on
        elif not s[i].isalpha():
            i += 1
        # if char at j is not alpha move on
        elif not s[j].isalpha():
            j -= 1

    return True

# print(validPalin("Ab$$  !b&%@a"))
# returns 'True' as expected

# print(validPalin("Ab$$ b&%c@a"))
# returns 'False' as expected
