# O(n)

def myPowBrute(x, n):
    if n == 0:
        return 1

    if n < 0:
        x = 1 / x
        n = -n

    ans = 1

    for i in range(n):
        ans = ans * x

    return ans


# O(log n), O(log n)
# recursive solution


def fastPow(x, n):
    if n == 0:
        return 1.0

    half = fastPow(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return half * half * x


def myPowRecursive(x, n):
    if n < 0:
        x = 1 / x
        n = -n

    return fastPow(x, n)


# O(log n), O(1)
# iterative solution

def myPowIterative(x, n):
    if n == 0:
        return 1.0

    if n == 1:
        return float(x)

    if n < 0:
        x = 1 / x
        n = -n

    current_product = x
    ans = 1

    while n:
        if n % 2 == 1:
            ans = ans * current_product

        current_product = current_product * current_product

        n = n // 2

    return ans
