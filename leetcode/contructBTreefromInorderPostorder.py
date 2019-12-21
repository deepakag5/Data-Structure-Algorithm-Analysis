def constructTreeRecursive(inorder, postorder):
    if not inorder or not postorder:
        return None

    ind = inorder.index(postorder.pop())
    root = Node(inorder[ind])
    root.right = constructTreeRecursive(inorder[ind + 1:], postorder)
    root.left = constructTreeRecursive(inorder[:ind], postorder)

    return root
