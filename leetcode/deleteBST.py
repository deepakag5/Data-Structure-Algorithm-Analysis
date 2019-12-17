def deleteRecursive(root, node):
    """

    :param root: TreeNode
    :param node: TreeNode
    :return: TreeNode

    """

    if root is None:
        return root

    if root.key > node.val:
        deleteRecursive(root.left, node)

    elif root.key < node.val:
        deleteRecursive(root.right, node)

    else:

        # if the node is with only one child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        if root.right is None:
            temp = root.left
            root = None
            return temp

        # if the node has two child then find the inorder successor
        temp = minValue(root.right)

        root.val = temp.val

        # delete the inorder successor
        root.right = deleteRecursive(root.right, temp)

    return root


def minValue(root):
    node = root

    while node.left is not None:
        node = node.left

    return node
