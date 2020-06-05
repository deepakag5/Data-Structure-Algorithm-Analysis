# Time: O(max(N,M))
# Space: O(max(N,M))


def addStrings(num1, num2):
    # edge cases
    if len(num1) == 0:
        return num2
    if len(num2) == 0:
        return num1

    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0:
        sum_val = carry

        if i >= 0:
            # ord will give the ascii value of char-int
            # we are getting difference of each one from 0
            # so that we get actual integer num
            # for example ascii value of 5 is 53 and that of 0 is 48
            # so 53-48 = 5 !!
            sum_val += ord(num1[i]) - ord('0')
            i -= 1
        if j >= 0:
            sum_val += ord(num2[i]) - ord('0')
            j -= 1

        # append the remainder (for example 12%10 we want to append 2)
        result.append(sum_val % 10)

        # get the quotient
        carry = sum_val // 10

    # if still carry has any value (which would have come from prev additions)
    if carry != 0:
        result.append(carry)

    # as we have started to add from the end we need to reverse and return as str
    return "".join(str(i) for i in result[::-1])
