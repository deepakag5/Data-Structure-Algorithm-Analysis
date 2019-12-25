def findtheCelebrity(n):
    candidate = 0

    # iterate the graph till we get such candidate which doesn't know previous one
    # this index will be for supposed celebrity
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    # iterate till the position of supposed celebrity and check
    # a) if supposed celebrity knows anybody before it or
    # b) if any of the other candidates doesn't know celebrity
    # if any of above condition if true return -1 (no celebrity)
    for i in range(candidate):
        if knows(candidate, i) or not knows(i, candidate):
            return -1
    # also check if any of the candidates after supposed celebrity doesn't know him
    # if yes then return -1 (no celebrity)
    for i in range(candidate+1, n):
        if not knows(i, candidate):
            return -1

    # if all above conditions are met then the supposed celebrity is actually the celebrity
    # return it
    return candidate