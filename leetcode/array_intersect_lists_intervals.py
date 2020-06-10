# Time Complexity: O(m+n)
# Space Complexity - O(m+n)


def intervalIntersection(A, B):
    if A is None:
        return B
    if B is None:
        return A

    i, j = 0, 0

    merge_list = []

    # Let's check if A[i] intersects B[j].
    # low - the startpoint of the intersection
    # high - the endpoint of the intersection
    while i < len(A) and j < len(B):
        low = max(A[i][0], B[j][0])
        high = min(A[i][-1], B[j][-1])

        if low <= high:
            merge_list.append([low, high])

        # Remove the interval with the smallest endpoint
        if A[i][-1] < B[j][-1]:
            i += 1
        else:
            j += 1

    return merge_list
