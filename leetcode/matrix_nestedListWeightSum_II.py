def depthSumInverse(nestedList):
    unweighted = 0
    weighted_res = 0

    while nestedList:
        nextlevel = []

        for item in nestedList:
            if item.isInteger():
                unweighted += item.getInteger()
            else:
                # or nextlevel += item.getList() 
                nextlevel.extend(item.getList())  # adding the items from the list t another list
        # adding the elements for each level visited
        weighted_res += unweighted
        nestedList = nextlevel

    return weighted_res
