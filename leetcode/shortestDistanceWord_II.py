def short(words, word1, word2):
    word_dict = {}

    for i, word in enumerate(words):
        if word == word1:
            if word1 in word_dict:
                word_dict[word1].append(i)
            else:
                word_dict[word1] = [i]

        elif word == word2:
            if word2 in word_dict:
                word_dict[word2].append(i)
            else:
                word_dict[word2] = [i]

    shortest_dist = float('inf')

    for word1_val in word_dict[word1]:
        for word2_val in word_dict[word2]:
            min_dist = abs(word1_val - word2_val)
            if min_dist < shortest_dist:
                shortest_dist = min_dist

    return shortest_dist
