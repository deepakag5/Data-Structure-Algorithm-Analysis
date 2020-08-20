# Time: O(n)
# Space: O(n)


def toGoatLatin(S):
    if len(S) == 0:
        return ""

    word_list = S.split()

    for i, word in enumerate(word_list):
        if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            word += "ma"
        else:
            first_char = word[0]
            word = word[1:] + first_char + "ma"

        word += "a" * (i + 1)

        word_list[i] = word

    return " ".join(word_list)
