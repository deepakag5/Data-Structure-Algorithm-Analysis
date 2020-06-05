def twoSum(arr, target):
    arr = sorted(arr)  # O (N log N)
    i, j = 0, len(arr) - 1
    ans = -1

    while i < j:
        if arr[i] + arr[j] < target:
            ans = max(ans, arr[i] + arr[j])
            i += 1
        else:
            j -= 1

    return ans
