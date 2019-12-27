def findLeaves(root):
    """
    :param root: TreeNode
    :return: List[List]
    """
    # create result list to hold the leaves at each height/depth
    res_list = []

    # do a dfs seach
    def find_height(node):
        if node is None:
            return 0

        # get the max height of the tree
        height = max(find_height(node.left), find_height(node.right))+1
        #print(height)

        # if result list has less items than height append for holding items for that height
        if len(res_list)<height:
            #print("in if")
            res_list.append([])

        # add node value to its level
        # remember level is height -1 (root level is considered as 0)
        res_list[height-1].append(node.val)
        #print(res_list)

        # this is collected by recursive calls made at line 15
        return height

    find_height(root)

    #print(res_list)
    return res_list
