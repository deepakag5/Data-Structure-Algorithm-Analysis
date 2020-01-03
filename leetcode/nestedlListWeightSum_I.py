def depthSum(nestedList):
    if len(nestedList) == 0:
        return 0

    depth, res = 1, 0

    while nestedList:
        res += depth * sum([x.getInteger() for x in nestedList if x.isInteger()])
        nestedList = sum([x.getList() for x in nestedList if not x.isInteger()], [])
        depth += 1

    return res
