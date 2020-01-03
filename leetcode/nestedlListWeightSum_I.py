def depthSum(nestedList):
    if len(nestedList) == 0:
        return 0

    depth, res = 1, 0

    while nestedList:
        res += depth * sum([x.getInteger() for x in nestedList if x.isInteger()])
        nestedList = sum([x.getList() for x in nestedList if not x.isInteger()], [])
        depth += 1

    return res


# Alternate using bfs

def depthSumbfs(self, nestedList):
    self.dfs(nestedList, 1)


def dfs(self, nestedList, level):
    sum = 0

    for n in nestedList:
        if n.isInteger():
            sum += n.getInteger() * level
        else:
            sum += self.dfs(n.getList(), level + 1)

    return sum
