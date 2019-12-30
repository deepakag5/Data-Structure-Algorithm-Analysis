# this is a problem of graph where the starting node is beginword and
# ending node is another node in the graph (wordlist values connected by one letter change)
# so we need to find shortest path between start and end node hence used BFS

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



