def deleteRecursive(root, node):
    """

    :param root: TreeNode
    :param node: TreeNode
    :return: TreeNode

    """

    if root is None:
        return root

    if root.val > node.val:
        root.left = deleteRecursive(root.left, node)

    elif root.val < node.val:
        root.right = deleteRecursive(root.right, node)

    else:
        # if the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # if the node has two child then find the inorder successor (smallest in right sub-tree)
        temp = minValue(root.right)

        # copy inorder successor to current node
        root.val = temp.val

        # delete the inorder successor
        root.right = deleteRecursive(root.right, temp)

    return root


def minValue(root):
    """

    :param root: TreeNode
    :return: TreeNode

    """
    node = root

    while node.left is not None:
        node = node.left
    print(node.val)

    return node
