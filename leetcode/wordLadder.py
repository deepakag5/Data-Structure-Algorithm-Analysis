# this is a problem of graph where the starting node is beginword and
# ending node is another node in the graph (wordlist values connected by one letter change)
# so we need to find shortest path between start and end node hence used BFS

# approach 1 - Brute force (replace each char and check)
import string


def findwordladder(beginWord, endWord, wordList):
    # set of word to remove duplicates
    wordSet = set(wordList)

    if endWord not in wordList:
        return 0

    # queue to iterate over the words in list
    queue = []

    queue.append(beginWord)

    # to hold the resulting number of iterations required
    res = 0

    # traverse for all the words
    while len(queue) > 0:
        for i in range(len(queue) - 1, -1, -1):
            word = queue.pop(0)
            # if word matches the endword we are looking for return
            if word == endWord:
                return res + 1
            # for all characters in word
            # replace each character by an alphabet (a-z)
            # if the word matched the word in word set and
            # it's not the current word add to the queue and
            # remove from wordset as it's already been visited
            for i in range(len(word)):
                char = list(word)
                charlist = string.ascii_lowercase[:26]

                for ch in charlist:
                    char[i] = ch
                    s = ''.join(char)
                    if s in wordSet and s != word:
                        queue.append(s)
                        wordSet.remove(s)


        res += 1

    return 0


# approach 2 - optimized by doing preprocessing of the word in the list
# instead of matching with word by replacing all of its character (one at a time)
# we match by a pattern as for Dot - *ot, D*t, Do*

# Do the pre-processing on the given wordList and find all the possible generic/intermediate states.
#  Save these intermediate states in a dictionary with key as the intermediate word and value as the list of words which have the same intermediate word.

# Push a tuple containing the beginWord and 1 in a queue. The 1 represents the level number of a node.
# We have to return the level of the endNode as that would represent the shortest sequence/distance from the beginWord.

# To prevent cycles, use a visited dictionary.

# While the queue has elements, get the front element of the queue. Let's call this word as current_word.

# Find all the generic transformations of the current_word and find out if any of these transformations is also a transformation of other words in the word list.
# This is achieved by checking the all_combo_dict.

# The list of words we get from all_combo_dict are all the words which have a common intermediate state with the current_word.
# These new set of words will be the adjacent nodes/words to current_word and hence added to the queue.

# Hence, for each word in this list of intermediate words, append (word, level + 1) into the queue where level is the level for the current_word.

# Eventually if you reach the desired word, its level would represent the shortest transformation sequence length.


from collections import defaultdict


def findwordladderOptimized(beginWord, endWord, wordList):
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0

    length_word = len(beginWord)

    all_comb_dict = defaultdict(list)

    for word in wordList:
        for i in range(length_word):
            all_comb_dict[word[:i] + "*" + word[i+1:]].append(word)

    queue = [(beginWord, 1)]

    visited = {beginWord: True}

    while queue:
        current_word, res = queue.pop(0)

        for i in range(length_word):
            intermediate_word = current_word[:i]+"*"+current_word[i+1:]

            for word in all_comb_dict[intermediate_word]:
                if word == endWord:
                    return res+1
                if word not in visited:
                    visited[word] = True
                    queue.append((word, res+1))

            all_comb_dict[intermediate_word] = []

    return 0


