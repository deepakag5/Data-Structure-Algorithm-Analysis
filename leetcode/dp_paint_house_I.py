def paintHouse(costs):
    if not costs or len(costs) == 0:
        return 0

    for i in range(1, len(costs)):
        print("before", " ", costs)
        costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
        costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
        costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        print("after", " ", costs)

    return min(costs[-1])


# O(1) space, shorter version, can be applied
# for more than 3 colors
def minCost(costs):
    if not costs:
        return 0
    dp = costs[0]
    for i in range(1, len(costs)):
        pre = list(dp)  # creates a shallow copy of dp
        for j in range(len(costs[0])):
            dp[j] = costs[i][j] + min(pre[:j] + pre[j + 1:])
    return min(dp)
