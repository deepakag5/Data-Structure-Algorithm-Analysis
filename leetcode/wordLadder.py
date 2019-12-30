def findwordladder(beginWord, endWord, wordList):
    wordSet = set(wordList)

    print(wordSet)

    if endWord not in wordList:
        return 0

    queue = []

    queue.append(beginWord)

    res = 0

    while len(queue) > 0:
        for i in range(len(queue) - 1, -1, -1):
            word = queue.pop(0)
            print(word)

    if word == endWord:
        return res + 1

    for i in range(len(word)):
        char = list(word)


    return 0



