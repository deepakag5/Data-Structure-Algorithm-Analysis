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


def mindepthBTreeIterative(root):
    """

    :param root: TreeNode
    :return: int

    """
    if not root:
        return 0

    depth = float('inf')
    stack = [(root, 1)]

    while stack:
        node, level = stack.pop()

        if node and not node.left and not node.right:
            depth = min(depth, level)

        if node:
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))

    return depth
