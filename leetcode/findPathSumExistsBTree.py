def findPathSumExistsRecursive(root, sum):
    """

    :param root: TreeNode
    :param sum: path sum value [int]
    :return: boolean

    """
    exist = []

    def findPathSum(root, target, exist):
        if root:
            if root.left is None and root.right is None:
                if root.val == target:
                    exist.append(True)
            if root.left is not None:
                findPathSum(root.left, target - root.val, exist)
            if root.right is not None:
                findPathSum(root.right, target - root.val, exist)

    findPathSum(root, sum, exist)

    return any(exist)
