def mindepthBTreeRecursive(root):
    """

    :param root: TreeNode
    :return: int

    """
    if root is None:
        return 0

    # in short we can also rewrite - if not root.left and not root.right
    if root.left is None and root.right is None:
        return 1

    if root.left is not None and root.right is None:
        return mindepthBTreeRecursive(root.left) + 1

    if root.left is None and root.right is not None:
        return mindepthBTreeRecursive(root.right) + 1

    return min(mindepthBTreeRecursive(root.left), mindepthBTreeRecursive(root.right)) + 1
