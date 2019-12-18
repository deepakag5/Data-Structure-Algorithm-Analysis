def calculateHeight(root):
    """
    :param root: TreeNode
    :return: int
    """

    if root.left is None and root.right is None:
        return 0

    left = 0
    if root.left is not None:
        left = calculateHeight(root.left)

    right = 0
    if root.right is not None:
        right = calculateHeight(root.right)

    return max(left, right) + 1
