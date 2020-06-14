# Time : O(S*n) On each step the algorithm finds the amount*num of coins
# Space : O(S) We use extra space for the memoization table.


def coinChange(coins, amount):
    # perform sort as we want to break when coin value is
    # greater than required amount
    coins.sort()
    # fill dp array with invalid values for amount+1 (array starts with 0)
    dp = [float('inf')] * (amount + 1)
    # for zero amount we need 0 coins
    dp[0] = 0

    for i in range(amount + 1):
        for j in range(len(coins)):
            # check only for coins where value is smaller than amount
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
            else:
                break
    # return dp[amount] value if we have overwritten it else -1
    return dp[amount] if dp[amount] != float('inf') else -1
