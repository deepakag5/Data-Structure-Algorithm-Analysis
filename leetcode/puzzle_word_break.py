# Time : O(n^2) Two loops are their to fill dp array
# Space : O(n) Length of p array is n+1


def word_break_dp(s, wordDict):
    if not wordDict:
        return False

    word_set = set(wordDict)

    dp = [False] * (len(s) + 1)
    # for empty string
    dp[0] = False

    for i in range(1, len(s) + 1):
        # for each substring (j,i) check if it exists in word_set
        # also, find if previous string was existing using dp[j]
        for j in range(i):
            if dp[j] and (s[j:i] in word_set):
                dp[i] = True
                break

    return dp[len(s)]
