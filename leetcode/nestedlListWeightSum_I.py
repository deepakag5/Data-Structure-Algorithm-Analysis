def depthSum(nestedList):
    if len(nestedList) == 0:
        return 0

    depth, res = 1, 0

    while nestedList:
        res += depth * sum([x.getInteger() for x in nestedList if x.isInteger()])
        nestedList = sum([x.getList() for x in nestedList if not x.isInteger()], [])
        depth += 1

    return res


# Alternate using dfs

def depthSumdfs(self, nestedList):
    self.dfs(nestedList, 1)


def dfs(self, nestedList, level):
    res = 0

    for n in nestedList:
        if n.isInteger():
            res += n.getInteger() * level
        else:
            res += self.dfs(n.getList(), level + 1)

    return res


def depthSumbfs(nestedList):
    stack = []
    res = 0
    level = 1

    for n in nestedList:
        stack.append((n, level))
    while stack:
        n, level = stack.pop(0)
        if n.isInteger():
            res += n.getInteger() * level
        else:
            for i in n.getList():
                stack.append((i, level + 1))

    return res