def maxDepthRecursive(root):
    """
    :param root: TreeNode
    :return: int
    """
    if root is None:
        return 0
    else:
        print("root: " + str(root.val))
        left_height = maxDepthRecursive(root.left)
        right_height = maxDepthRecursive(root.right)

        print("left: "+str(left_height))
        print("right: "+str(right_height))

    return max(left_height, right_height) + 1
