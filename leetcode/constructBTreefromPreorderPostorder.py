def constructTreeRecursive(preorder, postorder):
    """
    :param preorder: list
    :param postorder: list
    :return: TreeNode
    """
    if not postorder:
        return None
    elif len(postorder) == 1:
        return Node(preorder.pop(0))
    else:
        root = Node(preorder.pop(0))
        pos = postorder.index(preorder[0])
        root.left = constructTreeRecursive(preorder, postorder[:pos + 1])
        root.right = constructTreeRecursive(preorder, postorder[pos + 1:-1])
        return root


def constructTreeRecursiveOptimized(preorder, postorder):
    """
    :param preorder: list
    :param postorder: list
    :return: TreeNode
    """
    postorder_map = {}
    for i, num in enumerate(postorder):
        postorder_map[num] = i

    def constructTree(prestart, preend, poststart, postend):
        if prestart > preend:
            return None
        elif prestart == preend:
            return Node(preorder[prestart])
        else:
            # find the root node
            root = Node(preorder[prestart])
            # find the left sub tree root val
            left_val = preorder[prestart + 1]
            # find the length of left sub tree
            left_len = postorder_map[left_val] - poststart + 1
            # assign value to left and right sub trees
            root.left = constructTree(prestart + 1, prestart + left_len, poststart, poststart + left_len - 1)
            root.right = constructTree(prestart + left_len + 1, preend, poststart + left_len, postend - 1)
            return root

    return constructTree(0, len(preorder) - 1, 0, len(postorder) - 1)