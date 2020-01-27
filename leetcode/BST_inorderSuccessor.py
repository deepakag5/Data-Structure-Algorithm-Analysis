def inorderSuccesor(root, node):
    """
    :param root: TreeNode
    :param node: TreeNode
    :return: TreeNode
    """
    # if right child of node is
    # present then successor lies in right sub-tree
    if node.right is not None:
        return minValue(node.right)

    # if right child is not present then successor is one of the ancestors
    # traverse down the tree,
    # if a node’s data is greater than root’s data
    # then go right side,
    # otherwise go to left side.
    while root is not None:
        if node.val < root.val:
            succ = root
            root = root.left
        elif node.val > root.val:
            root = root.right
        else:
            break

    return succ


def minValue(node):
    """
    :param node: TreeNode
    :return: TreeNode
    """
    current = node

    while current is not None:
        if current.left is None:
            break
        current = current.left

    return current
