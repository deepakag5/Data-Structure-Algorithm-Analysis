# Time: O(N)
# Space: O(1)

def bestTime_BuySell(prices):
    # no data or one day data means no transactions so no profit
    if len(prices) <= 1:
        return 0

    max_profit = 0

    i = 0

    for j in range(1, len(prices)):
        # when price is lower on previous day buy and then sell on next day
        if prices[i] < prices[j]:
            max_profit += prices[j] - prices[i]

        i += 1

    return max_profit
