# Time : O(n)
# Space: O(1)
def stringUnique_NoExtraSpace(s):
    checker = 0

    for i in range(len(s)):
        value = ord(s[i]) - ord('a')  # ord('a')=97, ord('b')=98 and so on..  ord provides unicode


        # If bit corresponding to current character is already set
        # x & y Does a "bitwise and".
        # Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
        if (checker & (1 << value)) > 0:
            return False

        # set bit in checker
        checker |= (1 << value)  # equivalent to checker = checker | (1<<value)

    return True

# example

# 'abcd'

# checker = 0, 1<<value = 1, 0&1 = 0
# checker = 1, 1<<value = 2, 1&2 = 0
# checker = 3, 1<<value = 4, 2&4 = 0
# checker = 7, 1<<value = 8, 7&8 = 0
# return True

# 'abbcd'

# checker = 0, 1<<value = 1, 0&1 = 0
# checker = 1, 1<<value = 2, 1&2 = 0
# checker = 3, 1<<value = 2, 3&2 = 2
# return False
