def constructTreeRecursive(preorder, inorder):
    """
    :param preorder: list
    :param inorder: list
    :return: TreeNode
    """
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = Node(inorder[ind])
        root.left = constructTreeRecursive(preorder, inorder[0:ind])
        root.right = constructTreeRecursive(preorder, inorder[ind + 1:])

        return root


def constructTreeRecursiveOptimized(preorder, inorder):
    inorder_map = {}
    for i, num in enumerate(inorder):
        inorder_map[num] = i

    preorder_iter = iter(preorder)

    def constructTree(start, end):
        if start > end:
            return None
        root_val = next(preorder_iter)
        root = Node(root_val)
        ind = inorder_map[root_val]
        root.left = constructTree(start, ind - 1)
        root.right = constructTree(ind + 1, end)
        return root

    return constructTree(0, len(inorder) - 1)
