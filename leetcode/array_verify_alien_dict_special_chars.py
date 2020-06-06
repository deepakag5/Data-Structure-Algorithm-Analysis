# Time : O(c)
# Space: O(1)

# here the difference from verify alien dictionary is that
# the words could contain spaces, special characters, upper-case chars
import re


def verify_alien_dict(words, order):
    if len(words) <= 1:
        return True

    order_map = {}

    for i in range(len(order)):
        order_map[order[i]] = i

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        # select only the alphabets
        # method -1 - using re module findall method
        word1_alpha = "".join(re.findall("[a-zA-Z]", word1))

        # convert to lower case
        word1_alpha = word1_alpha.lower()

        # select only the alphabets
        # method -2 - using python built-in method isalpha
        word2_alpha = ""

        for char in word2:
            if char.isalpha():
                word2_alpha = "".join([word2_alpha, char])

        # convert to lower case
        word2_alpha = word2_alpha.lower()

        for j in range(min(len(word1_alpha), len(word2_alpha))):
            if word1_alpha[j] != word2_alpha[j]:
                if order_map[word1_alpha[j]] > order_map[word2_alpha[j]]:
                    return False
                break
        else:
            if len(word1_alpha) > len(word2_alpha):
                return False

    return True

# print(verify_alien_dict(words = ["H","he$%     llo","Leetode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
# gives result as 'True' as expected
