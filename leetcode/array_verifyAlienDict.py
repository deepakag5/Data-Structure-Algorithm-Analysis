# Time : O(c)
# Space: O(1)

def verifyAlienDict(words, order):
    # base case
    if len(words) <= 1:
        return words

    hash_map = {}

    for i in range(order):
        hash_map[order[i]] = i

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                if hash_map[word1[i]] > hash_map[word2[i]]:
                    return False
                break
        else:
            if len(word1) > len(word2):
                return False

    return True
