def constructTreeRecursive(inorder, postorder):
    """
    :param inorder: list
    :param postorder: list
    :return: TreeNode
    """
    if not inorder or not postorder:
        return None

    ind = inorder.index(postorder.pop())
    root = Node(inorder[ind])
    root.right = constructTreeRecursive(inorder[ind + 1:], postorder)
    root.left = constructTreeRecursive(inorder[:ind], postorder)

    return root


def constructTreeRecursiveOptimized(inorder, postorder):
    """
    :param inorder: list
    :param postorder: list
    :return: TreeNode
    """
    # use unordered map to find the index in O(1) time
    inorder_map = {}
    for i, num in enumerate(inorder):
        inorder_map[num] = i

    def constructTree(start, end):
        if start > end:
            return None
        root = Node(postorder.pop())
        ind = inorder_map[root.val]
        root.right = constructTree(ind + 1, end)
        root.left = constructTree(start, ind - 1)

        return root

    return constructTree(0, len(inorder) - 1)