def insertRecursive(root, node):
    """

    :param root: TreeNode
    :param node: TreeNode
    :return: TreeNode

    """

    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insertRecursive(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insertRecursive(root.left, node)

    return root
