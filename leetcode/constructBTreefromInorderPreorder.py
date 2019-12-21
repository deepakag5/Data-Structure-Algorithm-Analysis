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
