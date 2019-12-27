def findLeaves(root):
    """
    :param root: TreeNode
    :return: List[List]
    """
    res_list = []

    def find_height(node):
        if node is None:
            return 0

        height = max(find_height(node.left), find_height(node.right))+1
        #print(height)

        if len(res_list)<height:
            #print("in if")
            res_list.append([])

        res_list[height-1].append(node.val)
        #print(res_list)

        return height

    find_height(root)

    #print(res_list)
    return res_list


