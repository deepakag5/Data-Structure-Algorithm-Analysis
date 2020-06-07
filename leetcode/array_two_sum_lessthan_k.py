# Time: O(n log n)
# Space: O(1)


def twoSum(arr, target):
    arr = sorted(arr)  # O (N log N)
    i, j = 0, len(arr) - 1
    ans = -1

    while i < j:
        # as we have sorted if sum of the items
        # is less than target then get max till now
        # and increment left pointer
        if arr[i] + arr[j] < target:
            ans = max(ans, arr[i] + arr[j])
            i += 1
        # else the some is greater then target
        # so decrease right pointer
        else:
            j -= 1

    return ans
