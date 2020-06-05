# O(N^2)

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
            # min_dist = abs(word1_val-word2_val)
            # if min_dist<shortest_dist:
            #     shortest_dist = min_dist
            shortest_dist = min(shortest_dist, abs(word1_val - word2_val))

    return shortest_dist


# improved solution - O(N) for iterating dict + O(max(K,L) for if list pointer
# is bigger than every element of other list  , overall complexity O(N) + O(max(K,L)) = O(N)
# Space - O(N)

from collections import defaultdict


def shortestDist(words, word1, word2):
    """
    function where a word list is given along with two words in the list to find min distance between them
    :param words: list
    :param word1: str
    :param word2: str
    :return: int
    """

    def get_indices_list(word):
        """
        function to get indices of mathing word in words as a list
        :param word: str
        :return: list
        """
        word_dict = defaultdict(list)

        for i, w in enumerate(words):
            if w == word:
                word_dict[word].append(i)

        print(word_dict)
        return word_dict[word]

    list1, list2 = get_indices_list(word1), get_indices_list(word2)
    l1, l2 = 0, 0
    shortest_dist = float("inf")

    while l1 < len(list1) and l2 < len(list2):
        shortest_dist = min(shortest_dist, abs(list1[l1] - list2[l2]))
        if list1[l1] < list2[l2]:
            l1 += 1
        else:
            l2 += 1

    return shortest_dist
