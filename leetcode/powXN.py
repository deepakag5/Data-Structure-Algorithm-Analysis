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
        return 1

    half = fastPow(x, n / 2)

    if n % 2 == 0:
        return half * half
    else:
        return half * half * x


def myPowRecursive(x, n):
    if n < 0:
        x = 1 / x
        n = -n

    fastPow(x, n)
