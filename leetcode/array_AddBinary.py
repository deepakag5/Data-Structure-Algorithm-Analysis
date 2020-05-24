# Time : O(N+M)

def addBinary(a, b):
    return {'0:b'}.format(int(a, 2), int(b, 2))


# Time: O(max(N,M))
# Space: O(max(N,M))

def addBinary_bitbybit(a, b):
    # find the max len between a and b
    n = max(len(a), len(b))
    # make lengths similar by filling leading zeros
    a, b = a.zfill(n), b.zfill(n)

    carry = 0
    answer = []

    for i in range(n - 1, -1, -1):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1

        # if carry is not divisible by 2
        # meaning only one bit is 1 (1+0 = 1) scenario
        if carry % 2 == 1:
            answer.append('1')
        # (1+1 = 0 and carry 1 scenario)
        else:
            answer.append('0')

        # this makes carry hold the actual carry value
        # because 2//2 = 1 (and two will be case when there are two 1's)
        # but 1//2 = 0
        carry //= 2

    if carry == 1:
        answer.append('1')

    # because we are adding from end so we need to reverse
    # and output expects a string so join
    return "".join(answer[::-1])
