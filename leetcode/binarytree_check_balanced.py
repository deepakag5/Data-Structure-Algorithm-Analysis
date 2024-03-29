def isBalanced(root):
    """

    :param root: TreeNode
    :return: boolean

    """

    def check(root):

        if root is None:
            return 0

        left = check(root.left)
        right = check(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return 1

        return max(left + right) + 1

    return check(root) != -1


def isBalancedOptimized(root):
    """

    :param root: TreeNode
    :return: boolean

    """

    def check(root):
        if root is None:
            return 0

        left = check(root.left)
        if left == -1:
            return -1

        right = check(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return check(root) != -1
