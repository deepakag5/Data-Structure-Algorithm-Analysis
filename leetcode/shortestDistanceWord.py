# O(n^2)
def shortDist(words, w1, w2):

    if not words or not w1 or not w2:
        return ""

    shortestDist = len(words)

    for i in range(len(words)):
        if words[i]==w1:
            for j in range(len(words)):
                if words[j]==w2:
                    shortestDist = min(shortestDist, abs(i-j))


    return shortestDist


# O(n)
def shortDistOptimized(words, w1, w2):
    if not words or not w1 or not w2:
        return ""

    shortestDist = len(words)

    recent_i1, recent_i2 = -1, -1

    for i in range(len(words)):
        if words[i]==w1:
            recent_i1 = i

        elif words[i]== w2:
            recent_i2 = i

        if recent_i1!=-1 and recent_i2!=-1:
            shortestDist = min(shortestDist, abs(recent_i1-recent_i2))

    return shortestDist



def shortDistOptimized1(words, w1, w2):
    if not words or not w1 or not w2:
        return ""

    shortestDist = len(words)

    index1 = [i for i in range(len(words)) if words[i]==w1]
    index2 = [i for i in range(len(words)) if words[i]==w2]

    for i in index1:
        for j in index2:
            distance = abs(i-j)
            if distance<shortestDist:
                shortestDist = distance

    return shortestDist
