# Time : O(c)
# Space: O(1)


def verifyAlienDict(words, order):
    # base case
    if len(words) <= 1:
        return True

    hash_map = {}
    # we can also use enumerate here -- hash_map = {char:i for i, char in enumerate(order)}

    for i in range(len(order)):
        hash_map[order[i]] = i

    # using the transitive property a<=b and b<=c then a<=c
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        # check if the chars are not equal and if char for word1 is greater than word2
        # return False and break
        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                if hash_map[word1[i]] > hash_map[word2[i]]:
                    return False
                break
        # if the loop doesn't break then run else part and check for lengths
        # for cases like ["apple","app"] which should return false as "l">"blank char"
        else:
            if len(word1) > len(word2):
                return False

    return True