def sortArrayByParity(A):
    i = 0
    j = len(A) - 1

    while i <= j:
        if A[i] % 2 != 0 and A[j] % 2 == 0:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        elif A[i] % 2 == 0:
            i += 1
        elif A[j] % 2 != 0:
            j -= 1

    return A


def sortArrayByParity(A):
    even_arr = [i for i in A if i % 2 == 0]
    odd_arr = [i for i in A if i % 2 != 0]

    return even_arr.extend(odd_arr)
