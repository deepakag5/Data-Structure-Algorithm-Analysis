def deletedeepestNode(root, deep_node):
    """
    :param root: TreeNode
    :param deep_node: TreeNode
    :return: None
    """
    queue = []
    queue.append(root)

    while len(queue):
        temp = queue.pop(0)
        if temp is deep_node:
            temp = None
            return
        if temp.right:
            if temp.right is deep_node:
                temp.right = None
                return
            else:
                queue.append(temp.right)

        if temp.left:
            if temp.left is deep_node:
                temp.left = None
                return
            else:
                queue.append(temp.left)


def deleteNode(root, key):
    """
    :param root: TreeNode
    :param key: int
    :return: TreeNode
    """

    if root is None:
        return None

    if root.left is None and root.right is None:
        if root.val == key:
            return None
        else:
            return root

    key_node = None
    queue = []
    queue.append(root)

    while len(queue):
        temp = queue.pop(0)
        if temp.val == key:
            key_node = temp
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

    if key_node:
        x = temp.val
        deletedeepestNode(root, temp)
        key_node.val = x

    return root
