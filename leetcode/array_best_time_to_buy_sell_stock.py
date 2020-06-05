# Time : O(n^2)
# Space : O(1)
# brute force

def maxProfit(arr):
    maxprof = 0

    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j] - arr[i] > maxprof:
                maxprof = arr[j] - arr[i]

    return maxprof


# Time : O(n)
# Space : O(1)

def maxProfOptimized(arr):
    maxprof = 0
    minprice = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < minprice:
            minprice = arr[i]
        else:
            if arr[i] - minprice > maxprof:
                maxprof = arr[i] - minprice

    return maxprof
