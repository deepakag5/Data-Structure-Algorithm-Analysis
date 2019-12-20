def deleteNode(root, key):
    """
    :param root: TreeNode
    :param key: int
    :return: TreeNode
    """
    # if tree is empty there is nothing to delete
    if root is None:
        return None
    # if root has no child - either it can be equivalent to root or key not found
    if root.left is None and root.right is None:
        if root.val == key:
            return None
        else:
            return root

    # create a placeholder for node to be deleted (replaced with the data for deepest node)
    key_node = None
    queue = []
    queue.append(root)

    # traverse through the tree and find the node to be deleted
    while len(queue):
        temp = queue.pop(0)
        if temp.val == key:
            key_node = temp
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

    # if node is found (meaning key_node is not None)
    if key_node:
        x = temp.val  # save the value of rightmost/deepest node (temp) found by above traversal
        deletedeepestNode(root, temp)  # delete the deepest node
        key_node.val = x  # overwrite the node to be deleted with this deepest node data

    return root


def deletedeepestNode(root, deep_node):
    """
    :param root: TreeNode
    :param deep_node: TreeNode
    :return: None
    """
    queue = []
    queue.append(root)

    # keep traversing the tree until
    # deepest node is found
    while len(queue):
        temp = queue.pop(0)
        # if deepest node is found then delete it
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
