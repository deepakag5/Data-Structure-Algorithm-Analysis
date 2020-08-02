from collections import Counter
import re


def mostCommonWord(helpText, wordsToExclude):
    helpText = helpText[0].split()

    helpText1 = [re.sub('[^a-zA-Z]+', '', _) for _ in helpText]

    helpText1 = " ".join(helpText1)

    count = Counter(word for word in helpText1.lower().split())

    res, best = [], 0

    for word in count:
        if count[word] >= best and word not in wordsToExclude:
            res.append(word)
            best = count[word]

    return res


print(mostCommonWord([
                         "Purchase Order Item Help can't find item item is too much part of purchase need fix for image item delivered too fast purchase order too big is purchase order coming? Too big why?"],
                     ["help", "fix", "too", "is", "of"]))

codeList = [['apple', 'apple'], ['banana', 'anything', 'banana']]
shoppingCart = ['banana', 'orange', 'banana', 'apple', 'apple']


def checkList(codeList, shoppingCart):
    if len(codeList) == 0 or len(shoppingCart) == 0 or codeList is None or shoppingCart is None:
        return 0

    row, col, index = 0, 0, 0

    while row < len(codeList):
        col = 0

        while col < len(codeList[row]) and index < len(shoppingCart):

            if codeList[row][col] == shoppingCart[index] or codeList[row][col] == "anything":
                col += 1
                index += 1
            else:
                index += 1
            if index == len(shoppingCart) and (row < len(codeList) - 1) or col < len(codeList[row]):
                return 0
        row += 1

    return 1


print(checkList(codeList, shoppingCart))
