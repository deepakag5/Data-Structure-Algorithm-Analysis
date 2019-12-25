def shortDist(words, w1, w2):

    if not words or not w1 or not w2:
        return ""

    shortestDist = len(words)-1

    for i in range(len(words)):
        if words[i]==w1:
            for j in range(len(words)):
                if words[j]==w2:
                    shortestDist = min(shortestDist, abs(i-j))


    return shortestDist












