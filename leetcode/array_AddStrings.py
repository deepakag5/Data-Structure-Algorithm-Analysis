# Time: O(max(N,M))
# Space: O(max(N,M))

def addStrings(num1, num2):
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
            sum_val += ord(num1[i]) - '0'
            i -= 1
        if j >= 0:
            sum_val += ord(num2[i]) - '0'
            j -= 1

        result.append(sum_val % 10)

        carry = sum_val // 10

    if carry != 0:
        result.append(carry)

    return "".join(str(i) for i in result[::-1])
