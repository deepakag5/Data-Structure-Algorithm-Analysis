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


def calculateLevelSum(node, level, sum_level):
    """
    :param root: TreeNode
    :return:
    """
    if node is None:
        return

    sum_level[level] += node.val

    calculateLevelSum(node.left, level + 1, sum_level)
    calculateLevelSum(node.right, level + 1, sum_level)

    return sum_level

# levels = calculateHeight(root) + 1
# sum_levels = [0] * levels
# calculateLevelSum(root, levels, sum_levels)
