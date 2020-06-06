# Time : O(c)
# Space: O(1)

# here the difference from verify alien dictionary is that
# the words could contain spaces, special characters, upper-case chars

# Method 1  - Change in original word string
# We select only the alphabets and then compare them

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


# Method 2  - No change in original word string
# We do not select the alphabets instead just compare the words
# whenever there is a character skipping special chars


def verify_alien_dict_no_change_in_word(words, order):
    if len(words) <= 1:
        return True

    order_map = {}

    for i in range(len(order)):
        order_map[order[i]] = i

    for k in range(len(words) - 1):
        word1 = words[k]
        word2 = words[k + 1]

        # we need to convert to lower to match chars with dictionary !
        word1 = word1.lower()
        word2 = word2.lower()

        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            # compare only when both chars are alphabets
            if word1[i].isalpha() and word2[j].isalpha():
                if word1[i] != word2[j]:
                    if order_map[word1[i]] > order_map[word2[j]]:
                        return False
                    break
                i += 1
                j += 1
            # if char in word1 is not alpha skip and move forward only for word1
            elif not word1[i].isalpha():
                i += 1
            # if char in word2 is not alpha skip and move forward only for word2
            elif not word2[j].isalpha():
                j += 1
        # if all the characters are in order but word1 still have some characters left which are alpha
        # (remember we don't care if the word2 still has more characters because all the characters
        # have been visited for word2 in previous step and word1 still has some chars)
        else:
            if i < len(word1) and len(re.findall('[a-zA-Z]', word1[i:])) > 0:
                return False

    return True

# print(verify_alien_dict_no_change_in_word(words = ["App   ","app $"], order = "hlabcdefgijkmnopqrstuvwxyz"))
# gives result as 'True' as expected

# print(verify_alien_dict_no_change_in_word(words = ["Apple","app $l  %$$%^^"], order = "hlabcdefgijkmnopqrstuvwxyz"))
# gives result as 'False' as expected
